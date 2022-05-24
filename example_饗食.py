# -----------------------------------------------------------------------------#
# example:      饗食天堂
# -----------------------------------------------------------------------------#
from ReservationScripts.ReservationScript import Scripts

# input area
# -----------------------------------------------------------------------------#
INFO = {    "NEXT_MONTH": True,         # True: next month // False: this month
            "DATE"      : "23",         # Date-day
            "TIME"      : "17:30",      # time: 17:00/17:30/18:00/18:30/19:00
            "USER_NAME" : "0900000000", # user name
            "PASSWORDS" : "00000000",   # password
            "PEOPLE"    : "2",          # reservation seat(s)
            "CITY"      : "新竹市"      # restuarant location
        }
# timer : when to start
# -----------------------------------------------------------------------------#
from TimeControl import TimeControl
TimeControl.start_when("2022-05-24_10:32")

# script start
# -----------------------------------------------------------------------------#
Scripts.Paradise(INFO)