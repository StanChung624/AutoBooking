from sre_constants import BRANCH
from ..website_template.Inline import template_Inline

class SyaBuYo(template_Inline):
    """
        涮乃葉
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
    BRANCH_URL =   {    "新竹SOGO巨城店": "https://inline.app/booking/-LPimPrzunBVFBi0ckJB:inline-live-2a466/-LPjWTrlZSINZUYENhhS",
                        "欣欣百貨店"    : "https://inline.app/booking/-LPimPrzunBVFBi0ckJB:inline-live-2a466/-LPimPsuYiMGVUKKSBo8",
                        "汐止遠雄店"    : "https://inline.app/booking/-LPimPrzunBVFBi0ckJB:inline-live-2a466/-LPjTERhMC0ybw5aVUAy",
                        "統一時代市府店": "https://inline.app/booking/-LPimPrzunBVFBi0ckJB:inline-live-2a466/-LPjTo7xQo-PXZLfp52y",
                        "板橋中山遠百店（小遠百）": "https://inline.app/booking/-LPimPrzunBVFBi0ckJB:inline-live-2a466/-LPjUicKloDufblRzW7J",
                        "桃園台茂店"    : "https://inline.app/booking/-LPimPrzunBVFBi0ckJB:inline-live-2a466/-LPjVO9N3lZaaEkDWDl_",
                        "新竹大魯閣湳雅店": "https://inline.app/booking/-LPimPrzunBVFBi0ckJB:inline-live-2a466/-LPjXHFKw_bM0oQuKt2M",
                    }

    REQUIRED_INFO = {   "DATE"      : "2022-06-22",
                        "TIME"      : "11-45",
                        "NAME"      : "金城武",
                        "PEOPLE"    : "2",
                        "PHONE"     : "090000000",
                        "BRANCH"    : "新竹SOGO巨城店"                            
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

        # set url
        self.URL = self.BRANCH_URL[self.INFO["BRANCH"]]
    