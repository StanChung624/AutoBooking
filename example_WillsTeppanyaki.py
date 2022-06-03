# -----------------------------------------------------------------------------#
# example:      Will's Teppanyaki
# -----------------------------------------------------------------------------#
from ReservationScripts.Scripts import WillsTeppanyaki
# input area
# -----------------------------------------------------------------------------#
INFO = {    "DATE"      : "2022-06-22",
            "TIME"      : "11-45",
            "NAME"      : "金城武",
            "PHONE"     : "090000000",
            "PEOPLE"    : "2",            
        }
# script start
# -----------------------------------------------------------------------------#
WillsTeppanyaki().run(INFO, start_when="2022-05-24_15:37")