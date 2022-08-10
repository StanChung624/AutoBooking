# -----------------------------------------------------------------------------#
# example:      茶六
# -----------------------------------------------------------------------------#
from ReservationScripts.Scripts import Tea6
# input area
# -----------------------------------------------------------------------------#
INFO = {    "DATE"      : "2022-07-19",
            "TIME"      : "17-30",
            "NAME"      : "鍾OX",
            "PHONE"     : "0975723986",
            "PEOPLE"    : "2",
            "BRANCH"    : "朝富店"
        }
# script start
# -----------------------------------------------------------------------------#
Tea6().run(INFO, start_when="2022-06-22_15:50:40")