from ..website_template.Inline import template_Inline
from DriverSetup import *

class MoMoParadise(template_Inline):
    """
        Mo-Mo Paradise
                tested on chrome v.100 / at 2022.05.25
    Auto run with set scripts.
    
    Parameters
    ----------
        INFO : dict 
            refer to REQUIRED_INFO as an example. When missing key(s), user will be asked for input.

        start_when : str
            in the format of "YYYY-mm-dd_HH:MM"
    """
    INFO = None
    BRANCH_URL =   {    "新竹巨城牧場"  : "https://inline.app/booking/-KlcGro3QpVV0OQ_gRcI:inline-live-humaxasia/-LHHPxqdZqtKMq-y25le", 
                        "台北京站牧場"  : "https://inline.app/booking/-KlcGro3QpVV0OQ_gRcI:inline-live-humaxasia/-KlcGro3QpVV0OQ_gRcJ",
                        "高雄夢時代牧場": "https://inline.app/booking/-KlcGro3QpVV0OQ_gRcI:inline-live-humaxasia/-LJMypNLpzgRz24B6_Wy",
                        "統一時代牧場"  : "https://inline.app/booking/-KlcGro3QpVV0OQ_gRcI:inline-live-humaxasia/-LLguxO9H24QZ0t7wxtD",
                        "桃園統領牧場"  : "https://inline.app/booking/-KlcGro3QpVV0OQ_gRcI:inline-live-humaxasia/-LQHpNrnmS7FOAiWsKeq",
                        "中山牧場"      : "https://inline.app/booking/-KlcGro3QpVV0OQ_gRcI:inline-live-humaxasia/-LUY7bWeyKt7usH5MFpw",
                    }

    REQUIRED_INFO = {   "DATE"      : "2022-06-22",
                        "TIME"      : "11-45",
                        "NAME"      : "金城武",
                        "PEOPLE"    : "2",
                        "PHONE"     : "090000000",
                        "BRANCH"    : "公益店"                            
                    }

    # -----------------------------------------------------------------------------#
    # __init__ and launcher is defined in Script_default.py
    # -----------------------------------------------------------------------------#

    def check_data(self):
        def check_INFO():
            for key in self.REQUIRED_INFO.keys():
                if key not in self.INFO:
                    print("missing: ", key)
                    print("for example: ", self.REQUIRED_INFO[key])
                    self.INFO[key] = str(input("please insert manually:\n"))
            print(self.INFO)

        def check_url():
            if self.INFO['BRANCH'] not in self.BRANCH_URL:
                print('current branch url is not in the database, please enter manually:')
                print('for example: https://inline.app/booking/-KlcGro3QpVV0OQ_gRcI:inline-live-humaxasia/-LHHPxqdZqtKMq-y25le')
                self.BRANCH_URL[self.INFO['BRANCH']] = str(input(':\n'))

        check_INFO()
        check_url()