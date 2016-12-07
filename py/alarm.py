# alarm type and their code number
# code rule:
#       100(tpye) + 1(sub-type) e.x. 102
#    100000(type) + 1000 (sub-type) e.x. 103000
#
# if you want to have your own customized false alarm
# type = [code, url_base_result, url_target_result]

import falsealarm


def supress_false_alarm(entries_potential_regression, cid, kernel, submission):
    """
    supress false alarm if possible
    re-set the value of flag_compare_result as True (no potential regression)
    if all testing entries matches false alarm entries

    return True if all entries are in false alarm list
    """
    flag_compare_result = True # no regression
    for entry in entries_potential_regression:
        if falsealarm.false_alarm_entries.has_key(kernel):
            cid_dist = falsealarm.false_alarm_entries[kernel]
            if cid_dist.has_key(cid):
                submission_dist = cid_dist[cid]
                if submission_dist.has_key(submission):
                    false_alarm_entries = submission_dist[submission]
                    if not (entry in false_alarm_entries):
                        flag_compare_result = flag_compare_result and False
                else:
                    flag_compare_result = False
            else:
                flag_compare_result = False
        else:
            flag_compare_result = False

    return flag_compare_result

