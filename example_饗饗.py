# -----------------------------------------------------------------------------#
# example:      饗饗
# -----------------------------------------------------------------------------#
from ReservationScripts.Scripts import InParadise

# input area
# -----------------------------------------------------------------------------#
INFO = {    "NEXT_MONTH": True,         # True: next month // False: this month
            "DATE"      : "23",         # Date-day
            "TIME"      : ["17:30", "18:00"],      # time: 17:00/17:30/18:00/18:30/19:00
            "USER_NAME" : "0900000000", # user name
            "PASSWORDS" : "00000000",   # password
            "PEOPLE"    : "2",          # reservation seat(s)
            "CITY"      : "台北市",      # restuarant location
            "BRANCH"    : "微風店",      # full-name of the branch-store
            "MEALTIME"  : "午餐",        # 午餐/下午餐/晚餐
        }
# script start
# -----------------------------------------------------------------------------#
InParadise(INFO, start_when="2022-05-25_00:00")