# alarm type and their code number
# code rule:
#       100(tpye) + 1(sub-type) e.x. 102
#    100000(type) + 1000 (sub-type) e.x. 103000
#
# if you want to have your own customized false alarm
# type = [code, url_base_result, url_target_result]


OPCV_HIGH_1 = 101
FWTS_HIGH_1 = 201
FWTS_HIGH_2 = 202 # Identical fwts error detected and supressed
MEMORY_1 = 301
STATUS_1 = 401
ETHERNET_1 = [501,
                "https://certification.canonical.com/hardware/201208-11458/submission/102899/test/57863/result/7566195/",
                "https://certification.canonical.com/hardware/201208-11458/submission/106400/test/57863/result/7819455/"]

