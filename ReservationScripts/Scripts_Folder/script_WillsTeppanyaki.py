from ..website_template.Inline import template_Inline

class WillsTeppanyaki(template_Inline):
    """
        Will's Teppanyaki
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

    URL = "https://inline.app/booking/-MlIX9yWDwI6MUkexSdA:inline-live-2/-MlIXA7xzJCN7mVDVBjA"

    REQUIRED_INFO =  {  "DATE"      : "2022-06-28",
                        "TIME"      : "11-45",
                        "NAME"      : "金城武",
                        "PHONE"     : "090000000",
                        "PEOPLE"    : "2",                        
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

        check_INFO()
        

