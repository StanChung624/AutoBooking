# -----------------------------------------------------------------------------#
# example:      旭集
# -----------------------------------------------------------------------------#
from ReservationScripts.Scripts import Sunrise

# input area
# -----------------------------------------------------------------------------#
INFO = {    "NEXT_MONTH": True,         # True: next month // False: this month
            "DATE"      : "24",         # Date-day
            "TIME"      : "17:30",      # time: 17:00/17:30/18:00/18:30/19:00
            "USER_NAME" : "0900000000", # user name
            "PASSWORDS" : "00000000",   # password
            "PEOPLE"    : "2",          # reservation seat(s)
            "CITY"      : "新竹縣",       # restuarant location
            "BRANCH"    : "旭集竹北店",
            "MEALTIME"  : "晚餐",        # 午餐/下午餐/晚餐
        }
# script start
# -----------------------------------------------------------------------------#
Sunrise().run(INFO, start_when="2022-05-25_00:00")