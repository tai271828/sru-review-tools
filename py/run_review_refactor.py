#!/usr/bin/python
"""SRU report review tool.

usage:
./run_review.py -b url_submission_base -r url_submission_review
-j base_kernel -k review_kernel
-s url_suffix_base -d url_suffix_review

=========
Examples:
=========

1. general case: compare two submission from two kernels

python run_review.py -u <username> -k <apikey> --batch_limit 0 -b 3.16.0-33.44 -r 3.16.0-34.45 -y-pass-150320.html
python run_review.py -u <username> -k <apikey> --batch_limit 0 -b 3.16.0-33.44 -r 3.16.0-34.45 -y pass-150320.html
note the first example with a suffix beginning with a dash to access
http://people.canonical.com/~hwcert/sru-testing/utopic/3.16.0-33.44/utopic-proposed-pass-150320.html
and the second will give
http://people.canonical.com/~hwcert/sru-testing/utopic/3.16.0-33.44/utopic-proposedpass-150320.html


2. (often use this) compare the latest submission against the golden submission

compare utopic 3.16.0-36.48 with golden submissions
python run_review.py -r 3.16.0-36.48 -u <username> -k <apikey> --batch_limit 0

python run_review.py -r 3.13.0-51.84~precise1 -u <username> -k <apikey> --batch_limit 0
python run_review.py -r 3.13.0-51.84 -u <username> -k <apikey> --batch_limit 0
python run_review.py -r 3.13.0-51.84 -u <username> -k <apikey> --batch_limit 0 --oem

===============================
HOW TO USE FALSE ALARM FILTER??
===============================
1. edit the file falsealm.py, add, append, modify or delete review entries
that you expect it is a false alarm
2. append the option --ffilter (false alarm filter) in the command line
3. That is it!! The entry will not be regarded as an potential regression when it was found.


For submission no.106962 of trusty kernel 3.13.0-70.113 against golden submission no.102877,

add this code snippet in falsealm.py

    "3.13.0-70.113": {
        "201201-10383": {
            "106962": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            }
    }  

Then try to apply these two commands and compare the result.
You will understand this feature with the result.



python run_review.py -r  3.13.0-70.113 -u <username> -k <apikey> --batch_limit 0
v.s.
python run_review.py -r  3.13.0-70.113 -u <username> -k <apikey> --batch_limit 0 --ffilter


The comparison of the result is:
    4,7d3
    < ===============================================
    < potential regression was observed. - 201201-10383
    < ===============================================
    < 
    14c10
    < there may be regressions. Review manually again.
    ---
    > review complete! no regression was observed.

Please note:
1. 201201-10383 is not highlighted as an potential regression case anymore (againt the kernel and submission)
2. the conlusion will say "review complete! no regression was observed." instead of "there may be regressions. Review manually again."




TODO:
    1. search TODO in the comment lol
    2. color highlight for some printing

"""

import re
import sys
import json
import logging
import argparse
import requests
from lxml import etree
from collections import OrderedDict

import alarm
import alarmtype

DEBUG = False
DEBUG_VERBOSE = True  # will be overridden by DEBUG
ARGS = None
LOGGER = logging.getLogger('my_logger')


class URLParser:

    """class to handle any URL tasks."""

    def __init__(self):
        """init method."""
        pass


class ReviewHelper:

    """class to review test results."""

    def __init__(self):
        """init method."""
        pass

    def review_single(self):
        """review one and only one report."""
        pass

    def review_batch(self):
        """review mutiple reports."""
        pass


class C3Helper:

    """class to request and parse C3 data.

    An abstract layer to handle all communication between C3.
    
    """

    def __init__(self):
        """init method."""
        pass


class ReviewReport:

    def __init__(self, url_submission_base, url_submission_review, distkernel, oem=False, single=False):
        if single:
            cid = distkernel
            self.cid_sub_base = {}
            self.cid_sub_review = {}
            self.cid_sub_base[cid] = url_submission_base
            self.cid_sub_review[cid] = url_submission_review
        else:
            # True for pass, False for fail
            self.flag_review_status = True
            self.url_submission_base = url_submission_base
            if url_submission_base:
                self.cid_sub_base = get_cid_to_submission_from_rpt(url_submission_base)
            else:
                self.cid_sub_base = get_cid_to_submission_from_golden(distkernel, oem)
            self.cid_sub_review = get_cid_to_submission_from_rpt(url_submission_review)
            self.validate_cid_sub()

    def validate_cid_sub(self):
        """
        validate the data ready to use or not
        the cid numbers should be the same
        between self.cid_sub_base and self.cid_sub_review
        """
        pass

    def review(self):
        # self.cid_sub_review and self.cid_sub_base are dictionaries.
        for cid in self.cid_sub_review:
            if cid in self.cid_sub_base:
                # remember sub_base and sub_review are
                # int for submission number
                sub_base = self.cid_sub_base.get(cid, None)
                sub_review = self.cid_sub_review.get(cid, None)
                if sub_base and sub_review:
                    # for submission is None, there is no test result
                    # then we skip to fetch the data from C3
                    self.review_one_machine(cid, sub_base, sub_review)
            else:
                print "missing golden submission or added a new test unit %s" % cid

    def review_one_machine(self, cid, sub_base, sub_review):
        """
        Review the report of one machine.

        Give submission numbers of both of base and the one waiting to review,
        and the CID of the machine. This method will print the review result.

        @param cid: CID of that machine.
        @type cid: integer.
        @param sub_base: <c3-sumission-URL>/<submission number of the base submission>.
        @type sub_base: integer.
        @param sub_review: <c3-sumission-URL>/<submission number of the target submission>.
        @type sub_review: integer.
        @return None
        """
        print "reviewing %s, base sumission: %s, review target: %s" % (cid, sub_base, sub_review)
        apidata_base = get_apidata_from_c3(cid, sub_base)
        apidata_review = get_apidata_from_c3(cid, sub_review)
        flag_compare_result, entries_potential_regression = compare_two_api_submission(apidata_base, apidata_review, cid)
        # TODO: this could be a option
        # re-set the value of flag_compare_result as True (no potential regression)
        # if all testing entries matches false alarm entries
        if ARGS.ffilter:
            flag_compare_result = alarm.supress_false_alarm(entries_potential_regression, cid, ARGS.reviewkernel, sub_review)

        if flag_compare_result:
            if DEBUG:
                print "no regression was observed. - %s" % cid
        else:
            self.flag_review_status = False
            print "==============================================="
            print "potential regression was observed. - %s" % cid
            print "==============================================="
            print ""

    def summarize(self):
        """
        after reviewing, check the review status,
        summarize the flow status and
        decide whether continuing the flow or not.
        """
        print ""
        print "==============================================="
        if self.flag_review_status:
            print "review complete! no regression was observed."
        else:
            print "there may be regressions. Review manually again."
        print "==============================================="


############################# C3 API #####################################
def get_submission(args, submission):
    """
    return submission in json format
    """
    api_uri = args.instance_uri + 'api/v1/testresults/?report=' + submission
    if DEBUG:
        print api_uri
    api_params = {'username': args.username,
                  'api_key': args.apikey,
                  'limit': args.batch_limit}
    result = requests.get(api_uri, params=api_params)
    json = result.json()
    return json


def get_apidata_from_c3(cid, submission):
    return get_submission(ARGS, submission)
###################### END of C3 API #####################################


def compare_two_api_submission(apidata_base, apidata_review, cid=None):
    """
    compare two submissions with the data downloaded via C3 api.

    @parm apidata_base: submission data in json format
    @parm apidata_review: submission data in json format

    return true if the script think the two submissions are identical
    and false in opposite.
    """
    # flag to show the whole result
    flag_compare_result = True
    entries_potential_regression = []
    # data validation: make sure the total number of testing entries is the same.
    if apidata_base['meta']['total_count'] != apidata_review['meta']['total_count']:
        print "test_item_no_total is not the same!"
        flag_compare_result = False

    # submission comparison: compare the testing entry status and details
    for tib in apidata_base['objects']:
        # tib: test_item_base
        # tir: test_item_review
        test_name = tib['test']['name']
        # TODO: really bad efficiency, try sorting first?
        for tir in apidata_review['objects']:
            # check the status of review candidate, not the base
            # a better way is to compare the status of both submissions
            test_status = tir['status']
            if tir['test']['name'] == test_name:
                if tir['comment'] != tib['comment'] and test_status == 'fail':
                    flag_compare_result = False
                    ##############################################################
                    # This print is the testing entry name you what to know.
                    ##############################################################
                    print(test_name)
                    entries_potential_regression.append(test_name)
                    #print "%s is not the same" % test_name
                    ##############################################################
                    # differnt smarter or detailed way to analyze the test comment
                    # you MAY want to modify code snippet
                    # TODO: to refactor this part so users could hook up their own
                    # review code snippet.
                    ##############################################################
                    if test_name == 'graphics/screenshot_opencv_validation':
                        print "======= highlight opencv failures, please take a look ======="
                        print "============= base test ==============="
                        print tib['comment']
                        print "============= waiting to review ======="
                        print tir['comment']
                        print ""
                        entries_potential_regression.append(alarmtype.OPCV_HIGH_1)
                    if test_name == 'suspend/suspend-single-log-check':
                        # replace the time stamps to avoid noises
                        tib['comment'] = re.sub('\[ +[0-9.]+\]', '[TIMESTAMP]', tib['comment'])
                        tir['comment'] = re.sub('\[ +[0-9.]+\]', '[TIMESTAMP]', tir['comment'])
                        # split and sort test reports to get the same order
                        list_b = tib['comment'].split('\n')
                        list_r = tir['comment'].split('\n')
                        list_b.sort()
                        list_r.sort()
                        # highlight fwts caused failures
                        if list_b != list_r:
                            print "----- highlight fwts caused failures, please take a look -----"
                            print "============= base result ============"
                            print tib['comment']
                            print "============= review candidate ======="
                            print tir['comment']
                            print ""
                            entries_potential_regression.append(alarmtype.FWTS_HIGH_1)
                        else:
                            print "Identical fwts error detected and supressed"
                            entries_potential_regression.append(alarmtype.FWTS_HIGH_2)
                    if test_name == 'memory/info':
                        # memory failure and often to show little different details
                        # for example,
                        # Meminfo reports 572.82MiB less than lshw... v.s.
                        # Meminfo reports 572.81MiB less than lshw...
                        # This may give too many false alarms so I want to
                        # have a prompt message
                        print "memory/info comment comparison failed but please note the difference may be little."
                        entries_potential_regression.append(alarmtype.MEMORY_1)

                if tib['status'] != test_status:
                    # we want to compare the status of two submissions
                    print "test status changes : %s from %s to %s" % (test_name, tib['status'], tir['status'])
                    flag_compare_result = False
                    entries_potential_regression.append(alarmtype.STATUS_1)

                if DEBUG and DEBUG_VERBOSE:
                    print test_name, test_status

    return (flag_compare_result, entries_potential_regression)


def get_cid_to_submission_from_rpt(url):
    """
    get a association table cid v.s. submission
    hold the data by self.dict_rpt

    @parem dict_rpt: dict_rpt[cid] = submission
    @type dict_rpt: dict_rpt[cid] = submission, cid and submission are integers.
    """
    dict_rpt = {}
    parser = etree.HTMLParser()
    tree = etree.parse(url, parser)
    # the way to analyze the html table is horrible!
    for td in tree.xpath('/html/body/div/table/tr'):
        cid = None
        submission = None
        if td[1].getchildren():  # cid in 2nd td, with an <a>
            cid = td[1][0].text
            if td[3].getchildren():  # submission in 4th td, with an <a>
                submission = td[3][0].attrib['href'].split('/')[-2]
                dict_rpt[cid] = submission
            else:
                print ("No test result available for %s" % cid)
    return dict_rpt


def get_cid_to_submission_from_golden(distkernel, oem=False):
    dict_rpt = {}
    cs = None
    with open("../data/golden-submission.txt", "r") as data_file:
        json_contents = json.load(data_file)
    if distkernel == "vivid":
        cs = json_contents["vivid-3.19"]
    elif distkernel == "utopic":
        cs = json_contents["utopic-3.16"]
    elif distkernel == "trusty":
        cs = json_contents["trusty-3.13"]
    elif distkernel == "precise":
        cs = json_contents["precise-3.2"]
    elif oem:
        cs = json_contents["oem-trusty-3.19"]
    else:
        try:
            cs = json_contents[distkernel]
        except:
            LOGGER.critical("No such kernel available: %s" % distkernel)
            sys.exit(1)
    for cid in cs:
        # TODO:
        # cs[cid][0] return string
        # e.g. "102848" instead of ["102848"] from
        # "201101-7178": ["102848"]
        # this is bad code I think
        dict_rpt[cid] = cs[cid][0]

    return dict_rpt


def main():
    logging.basicConfig(level=logging.ERROR)
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group_cid_reviewkernel = parser.add_mutually_exclusive_group()
    parser.add_argument('--batch_limit', type=int, default=1,
                        help='Number of element in a batch result. \
                        0 for as many as possible')
    parser.add_argument('--instance_uri',
                        default="https://certification.canonical.com/",
                        help='Certification site URI. ')
    group.add_argument('-b', '--basekernel', help='base kernel, e.g. 3.16.0-33.44')
    group_cid_reviewkernel.add_argument('-r', '--reviewkernel', help='review kernel, e.g. 3.16.0-34.45')
    parser.add_argument('-y', '--suffixbase',
                        help='base filename suffix',
                        default=".html")
    parser.add_argument('-z', '--suffixreview',
                        help='review filename suffix',
                        default=".html")
    group.add_argument('-g', '--golden',
                       help='review the report based on golden submissions',
                       default=True)
    group.add_argument('-s', '--single', type=str, nargs=2, help='review a single report by 2 different submissions.')
    group_cid_reviewkernel.add_argument('-c', '--cid', help='CID, use this together with single')
    parser.add_argument('-u', '--username', help='User name', required=True)
    parser.add_argument('-k', '--apikey', help='API key', required=True)
    parser.add_argument('-o', '--oem', action='store_true', help='Review OEM reports')
    parser.add_argument('--ffilter', action='store_true', help='false alarm filter')
    parser.add_argument('-m', '--mode',
                        default='all',
                        help='pass, fail or skipped. Default is all')
    parser.add_argument("-d", "--debug", help="Set debug mode",
                        #action='store_const', const=logging.DEBUG,
                        default=logging.WARNING)

    global ARGS
    ARGS = parser.parse_args()
    args = ARGS

    #kernel_base = "3.2.0-79.115"
    #kernel_review = "3.2.0-80.116"
    kernel_base = args.basekernel
    kernel_review = args.reviewkernel
    if args.single:
        kernel_review = "3.2.0-80.116" # fake kernel version
    kernel_short = kernel_review.split('.0-')[0]  # e.g. 3.13
    with open("../data/kernel-list.txt", "r") as kernel_list:
        json_contents = json.load(kernel_list)
    releases = OrderedDict(sorted(json_contents.items(),
                                  key=lambda t: t[1],
                                  reverse=True))
    # Get the dist / distkernel here
    if '~' in kernel_review:
        idx = releases.keys().index(kernel_short)
        for key in releases.keys()[idx + 1:]:
            if releases.get(key)[1]:
                dist = releases.get(key)[0]
                distkernel = dist + '-' + kernel_short
                break
    else:
        # non-LTS version, kernel number could be mapped with the distro name
        dist = releases.get(kernel_short)[0]
        distkernel = dist

    url_host = "http://people.canonical.com/~hwcert/sru-testing/"

    url_prefix = url_host + dist

    filename_prefix_base = distkernel + "-proposed"
    if args.oem:
        filename_prefix_review = distkernel + "-oem-test-proposed"
    else:
        filename_prefix_review = distkernel + "-proposed"
    #filename_suffix_base = "-pass-150320.html"
    #filename_suffix_review = ".html"
    filename_suffix_base = ARGS.suffixbase
    filename_suffix_review = ARGS.suffixreview
    filename_base = filename_prefix_base + filename_suffix_base
    filename_review = filename_prefix_review + filename_suffix_review

    if args.golden:
        url_submission_base = None
    else:
        url_submission_base = url_prefix + "/" + kernel_base + "/" + filename_base

    url_submission_review = url_prefix + "/" + kernel_review + "/" + filename_review

    if DEBUG:
        print url_submission_base, url_submission_review
        print distkernel

    if args.single:
        rrpt = ReviewReport(args.single[0], args.single[1], args.cid, single=True) 
        rrpt.review()
    else:
        rrpt = ReviewReport(url_submission_base, url_submission_review, distkernel, args.oem)
        rrpt.review()
        rrpt.summarize()


if __name__ == "__main__":
    main()
