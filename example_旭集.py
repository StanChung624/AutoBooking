# -----------------------------------------------------------------------------#
# example:      旭集
# -----------------------------------------------------------------------------#
from ReservationScripts.ReservationScript import Scripts

# input area
# -----------------------------------------------------------------------------#
INFO = {    "NEXT_MONTH": True,         # True: next month // False: this month
            "DATE"      : "24",         # Date-day
            "TIME"      : "17:30",      # time: 17:00/17:30/18:00/18:30/19:00
            "USER_NAME" : "0900000000", # user name
            "PASSWORDS" : "00000000",   # password
            "PEOPLE"    : "2",          # reservation seat(s)
            "CITY"      : "新竹縣"      # restuarant location
        }
# script start
# -----------------------------------------------------------------------------#
Scripts.Sunrise(INFO, start_when="2022-05-24_10:32")