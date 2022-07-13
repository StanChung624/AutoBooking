# -----------------------------------------------------------------------------#
# example:      Will's Teppanyaki
# -----------------------------------------------------------------------------#
from ReservationScripts.Scripts import WillsTeppanyaki
# input area
# -----------------------------------------------------------------------------#
INFO = {    "DATE"      : "2022-08-08",
            "TIME"      : ["18-30", "18-00", "19-00"],
            "NAME"      : "鍾00",
            "PHONE"     : "0912345678",
            "PEOPLE"    : "2",            
        }
# script start
# -----------------------------------------------------------------------------#
WillsTeppanyaki().run(INFO, start_when="2022-06-24_23:59:59") 

WillsTeppanyaki().run(INFO, start_when="2022-06-24_23:59:59") 