# -----------------------------------------------------------------------------#
# example:      涮乃葉
# -----------------------------------------------------------------------------#
from ReservationScripts.Scripts import SyaBuYo
# input area
# -----------------------------------------------------------------------------#
INFO = {    "DATE"      : "2022-06-23",
            "TIME"      : "11-30",
            "NAME"      : "鍾XO",
            "PEOPLE"    : "2",
            "PHONE"     : "0900000000",
            "BRANCH"    : "新竹SOGO巨城店",
        }

# script start
# -----------------------------------------------------------------------------#
SyaBuYo().run(INFO, start_when="2022-06-04_16:35:45")