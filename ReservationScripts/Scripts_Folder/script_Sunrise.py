from ..website_template.FeastTogether import template_FeastTogether

class Sunrise(template_FeastTogether):
    """
        旭集
                tested on chrome v.100 / at 2022.05.25
    Auto run with set scripts.

    Parameters
    ----------
        INFO : dict 
            refer to REQUIRED_INFO as an example. When missing key(s), user will be asked for input.

        start_when : str
            in the format of "YYYY-mm-dd_HH:MM"
    """
    REQUIRED_INFO = {   "NEXT_MONTH": True,         # True: next month // False: this month
                        "DATE"      : "23",         # Date-day
                        "TIME"      : "17:30",      # time: 17:00/17:30/18:00/18:30/19:00
                        "USER_NAME" : "0912345678", # user name
                        "PASSWORDS" : "abc12345",   # password
                        "PEOPLE"    : "2",          # reservation seat(s)
                        "CITY"      : "新竹縣",      # restuarant location
                        "BRANCH"    : "旭集竹北店",
                        "MEALTIME"  : "晚餐/午餐/下午餐",
                    }
    INFO = None
    URL = "https://www.feastogether.com.tw/booking/10"
    # -----------------------------------------------------------------------------#
    # __init__ and launcher is defined in Script_default.py
    # -----------------------------------------------------------------------------#
    def check_data(self):
        for key in self.REQUIRED_INFO.keys():
            if key not in self.INFO:
                print("missing: ", key)
                print("for example: ", self.REQUIRED_INFO[key])
                self.INFO[key] = str(input("please insert manually:\n"))
                # for the bool. value
                if key == "NEXT_MONTH" and self.INFO["NEXT_MONTH"] == "True":
                    self.INFO["NEXT_MONTH"] = True
                elif key == "NEXT_MONTH" and self.INFO["NEXT_MONTH"] == "False":
                    self.INFO["NEXT_MONTH"] = False
