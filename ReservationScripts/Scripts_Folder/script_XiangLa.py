from sre_constants import BRANCH
from ..website_template.Inline import template_Inline

class XianLa(template_Inline):
    """
        嚮辣
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
    BRANCH_URL =   {    "台中五權西店": "https://inline.app/booking/-MobhN-J_AL6rzXZg0VN:inline-live-2/-Mwa3wNxlGAlYAVckx-6",
                        "台北松江店"    : "https://inline.app/booking/-MobhN-J_AL6rzXZg0VN:inline-live-2/-MobhNDzUda6zAQ2Z1wp",
                        "台北捷運西門店"    : "https://inline.app/booking/-MobhN-J_AL6rzXZg0VN:inline-live-2/-N4ITT0JEyOWTbxEbYca",
                    }

    REQUIRED_INFO = {   "DATE"      : "2022-06-22",
                        "TIME"      : "11-45",
                        "NAME"      : "金城武",
                        "PEOPLE"    : "2",
                        "PHONE"     : "090000000",
                        "BRANCH"    : "台中五權西店"                            
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

        def check_url():
            if self.INFO['BRANCH'] not in self.BRANCH_URL:
                print('current branch url is not in the database, please enter manually:')
                print('for example: https://inline.app/booking/-MobhN-J_AL6rzXZg0VN:inline-live-2/-Mwa3wNxlGAlYAVckx-6')
                self.BRANCH_URL[self.INFO['BRANCH']] = str(input(':\n'))

        check_INFO()
        check_url()

        # set url
        self.URL = self.BRANCH_URL[self.INFO["BRANCH"]]
    