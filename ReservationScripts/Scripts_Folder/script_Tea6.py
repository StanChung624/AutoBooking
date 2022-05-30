from ..website_template.Inline import template_Inline

class Tea6(template_Inline):
    """
        茶六
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
    BRANCH_URL =   {    "公益店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-LUYUEIOYwa7GCUpAFWA",
                        "朝富店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-L93VSXuz8o86ahWDRg1",
                        "中清店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-MNhWoTy962xAuCH9tCh",
                        "博愛店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-LAIJeeZ-6rG3IpB1KUE",
                    }

    REQUIRED_INFO =  {  "DATE"      : "2022-05-28",
                        "TIME"      : "11-45",
                        "NAME"      : "金城武",
                        "PHONE"     : "090000000",
                        "PEOPLE"    : "2",
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

        def check_url():
            if self.INFO['BRANCH'] not in self.BRANCH_URL:
                print('current branch url is not in the database, please enter manually:')
                print('for example: https://inline.app/booking/-LPimPrzunBVFBi0ckJB:inline-live-2a466/-LPjWTrlZSINZUYENhhS')
                self.BRANCH_URL[self.INFO['BRANCH']] = str(input(':\n'))

        check_INFO()
        check_url()

