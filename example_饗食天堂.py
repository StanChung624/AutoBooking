# -----------------------------------------------------------------------------#
# example:      饗食天堂
# -----------------------------------------------------------------------------#
from ReservationScripts.Scripts import Paradise

# input area
# -----------------------------------------------------------------------------#
INFO = {    "NEXT_MONTH": True,         # True: next month // False: this month
            "DATE"      : "20",         # Date-day
            "TIME"      : "11:30",      # time: 17:00/17:30/18:00/18:30/19:00
            "USER_NAME" : "0900000000", # user name
            "PASSWORDS" : "00000000",   # password
            "PEOPLE"    : "2",          # reservation seat(s)
            "CITY"      : "台北市",      # restuarant location
            "BRANCH"    : "京站店",
            "MEALTIME"  : "午餐",        # 午餐/下午餐/晚餐
        }
# script start
# -----------------------------------------------------------------------------#
Paradise().run(INFO, start_when="2022-05-25_00:00")