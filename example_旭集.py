# -----------------------------------------------------------------------------#
# example:      旭集
# -----------------------------------------------------------------------------#
from ReservationScripts.ReservationScript import Scripts

# input area
# -----------------------------------------------------------------------------#
INFO = {    "NEXT_MONTH": True, # True: next month // False: this month
            "DATE"      : "24",       # Date-day
            "TIME"      : "17:30",    # time: 17:00/17:30/18:00/18:30/19:00
            "USER_NAME" : "0975723986", # user name
            "PASSWORDS" : "pigs7321",   # password
            "PEOPLE"    : "2",             # reservation seat(s)
            "CITY"      : "新竹縣"           # restuarant location
    }
# timer : when to start
# -----------------------------------------------------------------------------#
from TimeControl import TimeControl
TimeControl.start_when("2022-05-25_00:00")

# script start
# -----------------------------------------------------------------------------#
Scripts.Sunrise(INFO)