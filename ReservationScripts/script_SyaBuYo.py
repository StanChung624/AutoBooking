from .template import Scripts_default
from DriverSetup import *

class SyaBuYo(Scripts_default):
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

    def __init__(self, INFO:dict={}, start_when=False):
        self.luancher(INFO, start_when)
    
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

    def run(self):
        INFO = self.INFO
        # script start
        # -----------------------------------------------------------------------------#
        # open webpage
        driver = DriverSetup()
        
        driver.get(self.BRANCH_URL[INFO["BRANCH"]])
        sleep(0.5)
        driver.maximize_window()
        # fill-in people
        element = driver.find_element(By.XPATH, "//select[@class='sc-dJjYzT kxiniR']")
        Select(element).select_by_index(int(INFO['PEOPLE']))
        # fill-in date
        driver.find_element_then_click(By.XPATH, "//div[@class='sc-dJjYzT kxiniR']")
        driver.send_ScrollDown()
        driver.find_element_then_click(By.XPATH, "//div[@data-date='"+INFO["DATE"]+"']//span[1]")
        driver.find_element_then_click(By.XPATH, "//button[@data-cy='book-now-time-slot-box-"+INFO["TIME"]+"']")

        # fill-in user info
        driver.find_element_then_click(By.XPATH, "//span[text()='下一步，填寫聯絡資訊']")
        sleep(0.5)
        driver.find_element(By.ID, "name").send_keys(INFO["NAME"])
        driver.find_element(By.ID, "phone").send_keys(INFO["PHONE"])
        driver.find_element_then_click(By.XPATH, "//div[@value='朋友聚餐']")

        # final
        driver.find_element_then_click(By.XPATH, "(//label[@class='sc-bqiRlB fCuXci'])[2]")
        driver.find_element_then_click(By.XPATH, "//button[@class='sc-ieecCq eZhyRr']")

        driver.endDriver()