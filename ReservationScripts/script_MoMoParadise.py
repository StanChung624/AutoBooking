from .template import Scripts_default
from DriverSetup import *

class MoMoParadise(Scripts_default):
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

    def __init__(self, INFO:dict={}, start_when=False):
        self.luancher(INFO, start_when)

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
        # click purpose
        driver.find_element_then_click(By.XPATH, "//div[@value='朋友聚餐']")

        # final
        driver.find_element_then_click(By.XPATH, "(//label[@class='sc-bqiRlB fCuXci'])[2]")
        driver.find_element_then_click(By.XPATH, "//button[@class='sc-ieecCq eZhyRr']")

        driver.endDriver()