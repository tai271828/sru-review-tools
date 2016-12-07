# {
#   kernel :
#   { cid :
#       {target_submission : [entry1, entry2...]}
#   }
#}
#
import alarmtype

false_alarm_entries = {
    "3.13.0-66.108~precise1": {
        "201208-11458": {
            "106400" : ["ethernet/detect"]
            },
        "201207-11439": {
            "106343" : ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201303-13015": {
            "106380": ["graphics/screenshot_opencv_validation",
                        alarmtype.OPCV_HIGH_1,
                        alarmtype.STATUS_1,
                        "suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_1]
            },
        "201203-10664": {
            "106370": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_1]
            },
        "201308-14158": {
            "106385": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201307-13944": {
            "106337": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201308-14114": {
            "106387": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201302-12684": {
            "106388": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_1]
            },
        # all fwts medium
        "201209-11640": {
            "106359": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_1]
            },
        # no go into device difference
        "201201-10399": {
            "106408": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_1,
                        alarmtype.STATUS_1]
            },
        # memory differnce is very small
        "201209-11789": {
            "106365": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2,
                        "memory/info",
                        alarmtype.MEMORY_1]
            },
        # memory differnce is very small
        "201212-12396": {
            "106368": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2,
                        "memory/info",
                        alarmtype.MEMORY_1]
            },
        # no webcam anymore
        # this golden submission is wrong
        "201307-13943": {
            "106338": ["graphics/screenshot_opencv_validation",
                        alarmtype.OPCV_HIGH_1,
                        alarmtype.STATUS_1]
            },
        # no go into device difference
        "201206-11156": {
            "106358": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_1,
                        alarmtype.STATUS_1]
            },
        "201309-14175": {
            "106393": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            }
        },
    "3.19.0-31.36~14.04.1": {
        # no certification
        # based on golden submission review
        # obex time expected to be failed (?)
        # and the highlight caused by the ms(?)
        "201501-16341": {
            "106436" : ["suspend/bluetooth_obex_browse_after_suspend_auto",
                        "suspend/bluetooth_obex_browse_before_suspend",
                        "suspend/bluetooth_obex_get_after_suspend_auto",
                        "suspend/bluetooth_obex_get_before_suspend",
                        "suspend/bluetooth_obex_send_after_suspend_auto",
                        "suspend/bluetooth_obex_send_before_suspend",
                        "suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201201-10383": {
            "106404": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        # mount web cam so it get better
        "201209-11785": {
            "106439" : [alarmtype.STATUS_1]
            }
    },
    "3.19.0-31.36": {
        # no certification
        # based on golden submission review
        # obex time expected to be failed (?)
        # and the highlight caused by the ms(?)
        "201501-16341": {
            "106469" : ["suspend/bluetooth_obex_browse_after_suspend_auto",
                        "suspend/bluetooth_obex_browse_before_suspend",
                        "suspend/bluetooth_obex_get_after_suspend_auto",
                        "suspend/bluetooth_obex_get_before_suspend",
                        "suspend/bluetooth_obex_send_after_suspend_auto",
                        "suspend/bluetooth_obex_send_before_suspend",
                        "suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201201-10383": {
            "106460": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            }
    },
    ###############################################################
    # SRU 15W47-48 by Tai
    ###############################################################
    # precise 3.2
    "3.2.0-95.135": {
        "201103-7380": {
            "106866": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        # old issue, skip cpu_topology
        #"201005-5775": {
        #    "106997": ["teset status is not the same"]
        #    },
        "201101-6973": {
            # LP: #1517786
            "106820": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201105-8048": {
            # LP: #1517786
            "106819": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201104-7945": {
            "106868": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201101-6965": {
            "106857": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201104-7784": {
            # medium failure
            "106867": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2,
                        # medium failure
                        "suspend/network_resume_time_auto"]
            },
        "201101-7178": {
            # ethernet is good actually by manual check
            "102848": ["ethernet/detect"]
            },
        "201101-7173": {
            # the bad boy BCM wireless
            "102848": ["suspend/wireless_connection_after_suspend_open_bg_auto",
                       "suspend/wireless_connection_after_suspend_open_n_auto",
                       "suspend/wireless_connection_after_suspend_wpa_bg_auto",
                       "suspend/wireless_connection_after_suspend_wpa_n_auto"]
            },
        "201202-10550": {
            # LP: #1517786
            "106868": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1,
                        # 1 suspends took longer than 15.00 seconds. (x 1)
                        "spend/suspend-single-log-check"]
            },
        "201101-7181": {
            "106862": ["suspend/network_resume_time_auto"]
            }
    },
    # precise 3.13
    "3.13.0-70.113~precise1": {
        "201202-10548": {
            # LP: #1517786
            "106893": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        # memory differnce is very small
        "201212-12396": {
            "107065": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2,
                        "memory/info",
                        alarmtype.MEMORY_1]
            },
        # no webcam anymore
        # this golden submission is wrong
        "201307-13943": {
            "102914": ["graphics/screenshot_opencv_validation",
                        alarmtype.OPCV_HIGH_1,
                        alarmtype.STATUS_1]
            },
        # not go into device difference
        "201206-11156": {
            "107061": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_1,
                        alarmtype.STATUS_1]
            },
        "201309-14199": {
            # LP: #1517786
            "106912": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201203-10664": {
            # LP: #1517786
            "106896": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201209-11633": {
            # LP: #1517786
            "106902": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201210-11859": {
            # LP: #1517786
            "106906": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201304-13210": {
            # LP: #1517786
            "106914": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201304-12474": {
            # LP: #1517786
            "106922": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201307-13902": {
            # LP: #1517786
            "106904": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201203-10655": {
            # LP: #1517786
            "106894": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201308-14114": {
            # LP: #1517786
            "106915": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1,
                        "suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201307-13944": {
            # LP: #1517786
            "106906": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1,
                        "suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201206-11156": {
            # LP: #1517786
            "106910": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1,
                        "suspend/suspend-single-log-check"]
            },
        "201308-14185": {
            "106928": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201209-11640": {
            "107069": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201304-13407": {
            "106901": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201307-14029": {
            "106924": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201308-14158": {
            "106928": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201303-13015": {
            # this desktop did not connect webcam physically
            "107042": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2,
                        "graphics/screenshot_opencv_validation",
                        alarmtype.OPCV_HIGH_1]
            },
        "201309-14175": {
            "106916": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2,
                        # LP: #1517786
                        "suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            },
        "201302-12728": {
            # LP: #1517786
            "106913": ["suspend/network_before_suspend",
                        alarmtype.STATUS_1]
            }
    },
    # trusty
    "3.13.0-70.113": {
        "201201-10383": {
            "106962": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            }
    },
    # trusty 3.19
    "3.19.0-37.42~14.04.1": {
        # no certification
        # based on golden submission review
        # obex time expected to be failed (?)
        # and the highlight caused by the ms(?)
        "201501-16341": {
            "107028" : ["suspend/bluetooth_obex_browse_after_suspend_auto",
                        "suspend/bluetooth_obex_browse_before_suspend",
                        "suspend/bluetooth_obex_get_after_suspend_auto",
                        "suspend/bluetooth_obex_get_before_suspend",
                        "suspend/bluetooth_obex_send_after_suspend_auto",
                        "suspend/bluetooth_obex_send_before_suspend",
                        "suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201201-10383": {
            "107019": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        # mount web cam so it get better
        "201209-11785": {
            "107023" : [alarmtype.STATUS_1]
            }
    },
    # trusty 4.2
    "4.2.0-19.23~14.04.1": {
        "201201-10383": {
            "107093": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            }
    },
    # vivid
    "3.19.0-37.42": {
        # no certification
        # based on golden submission review
        # obex time expected to be failed (?)
        # and the highlight caused by the ms(?)
        "201501-16341": {
            "107060" : ["suspend/bluetooth_obex_browse_after_suspend_auto",
                        "suspend/bluetooth_obex_browse_before_suspend",
                        "suspend/bluetooth_obex_get_after_suspend_auto",
                        "suspend/bluetooth_obex_get_before_suspend",
                        "suspend/bluetooth_obex_send_after_suspend_auto",
                        "suspend/bluetooth_obex_send_before_suspend",
                        "suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            },
        "201201-10383": {
            "107048": ["suspend/suspend-single-log-check",
                        alarmtype.FWTS_HIGH_2]
            }
    }
}
