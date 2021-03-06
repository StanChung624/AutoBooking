# -----------------------------------------------------------------------------#
# example:      Mo-Mo Paradise
# -----------------------------------------------------------------------------#
from ReservationScripts.Scripts import MoMoParadise
# input area
# -----------------------------------------------------------------------------#
INFO = {    "DATE"      : "2022-05-25",
            "TIME"      : ["17-15", "17-00"],
            "NAME"      : "金城武",
            "PEOPLE"    : "2",
            "PHONE"     : "0900000000",
            "BRANCH"    : "新竹巨城牧場",
        }

# script start
# -----------------------------------------------------------------------------#
MoMoParadise().run(INFO, start_when="2022-05-25_08:51")