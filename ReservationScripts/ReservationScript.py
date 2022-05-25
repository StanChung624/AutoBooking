from DriverSetup import *
from TimeControl import TimeControl

# -----------------------------------------------------------------------------#
# default scripts luancher
# -----------------------------------------------------------------------------#
from time import time
class Scripts_default:
    def luancher(self, INFO, start_when):
        # INFO checked
        self.INFO = INFO
        self.check_data()

        # wait until given start_when
        if start_when:
            TimeControl.start_when(start_when)

        # timer - start
        tic = time()

        # For single reservation time:        
        if isinstance(INFO["TIME"], str):
            self.run()

        # For multiple reservation time:
        elif isinstance(INFO["TIME"], list):
            TIME_LIST = INFO["TIME"]
            for i in range(len(TIME_LIST)):
                INFO["TIME"] = TIME_LIST[i]
                try:
                    self.run()
                    return
                except:
                    continue
        
        elapse = time() - tic
        print("elapse time: ", elapse, ' (sec.)')
# -----------------------------------------------------------------------------#
# Scripts starts
# -----------------------------------------------------------------------------#
class Scripts:

    class Sunrise(Scripts_default):
        """
            旭集
                    tested on chrome v.100 / at 2022.05.25
        Auto run with set scripts.
        :args:
            -INFO: (dict) object with REQUIRED_INFO, when missing key(s), user will be asked for input.
            -start_when: (str) in the format of "YYYY-mm-dd_HH:MM"
        """
        REQUIRED_INFO = {   "NEXT_MONTH": True,         # True: next month // False: this month
                            "DATE"      : "23",         # Date-day
                            "TIME"      : "17:30",      # time: 17:00/17:30/18:00/18:30/19:00
                            "USER_NAME" : "0912345678", # user name
                            "PASSWORDS" : "abc12345",   # password
                            "PEOPLE"    : "2",          # reservation seat(s)
                            "CITY"      : "新竹市"      # restuarant location
                        }
        INFO = None
        URL = "https://www.feastogether.com.tw/booking/10"

        def __init__(self, INFO:dict={}, start_when=False):
            self.luancher(INFO, start_when)

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

        def run(self):
            INFO = self.INFO
            # script start
            # -----------------------------------------------------------------------------#
            # open webpage
            driver = DriverSetup()
            driver.get(self.URL)
            driver.maximize_window()

            # click pop-up notification
            sleep(0.5)
            driver.find_element_then_click(By.XPATH, "//div[@id='modal-news']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]")

            # fill-in imformation
            driver.find_element_then_click(By.ID, "select_area")
            driver.find_element_then_click(By.XPATH, "//li[text()='"+INFO["CITY"]+"']")
            driver.find_element(By.ID, "book_people").send_keys(INFO["PEOPLE"])
            driver.find_element_then_click(By.XPATH, "//input[contains(@class,'flatpickr flatpickr-input')]")
            sleep(0.5)
            if INFO["NEXT_MONTH"]:
                driver.find_element_then_click(By.CLASS_NAME, "flatpickr-next-month")
            sleep(0.5)
            driver.find_element_then_click(By.XPATH, "(//span[text()='"+INFO["DATE"]+"'])[2]")
            driver.find_element_then_click(By.CLASS_NAME, "wk-type-dinner")

            # bottom choose store
            driver.send_ScrollDown()
            driver.send_ScrollDown()
            driver.find_element_then_click(By.XPATH, "//tr[@class='wk-book-stores list-tr']//td[1]")

            # log-in
            sleep(0.5)
            driver.find_element(By.XPATH, "(//input[@placeholder='手機'])[3]").send_keys(INFO["USER_NAME"])
            driver.find_element(By.XPATH, "(//input[@type='password'])[3]").send_keys(INFO["PASSWORDS"])
            driver.find_element_then_click(By.NAME, "login")
            sleep(0.5)

            # for the warning window (change password notification)
            try:
                driver.send_Enter(driver)
            except:
                pass

            sleep(0.5)

            # bottom choose store
            driver.find_element_then_click(By.XPATH, "//tr[@class='wk-book-stores list-tr']//td[1]")

            # choose reservation time
            order_time_element = driver.find_element(By.ID, "order_time")
            Select(order_time_element).select_by_visible_text(INFO["TIME"])

            # final: send_reservation
            sleep(0.5)
            driver.send_ScrollDown(4)
            sleep(0.5)
            driver.find_element_then_click(By.XPATH, "//button[@type='button']", loop_max=30)
            driver.endDriver()
    
    class Paradise(Scripts_default):
        """
            饗食天堂
                    tested on chrome v.100 / at 2022.05.25
        Auto run with set scripts.
        :args:
            -INFO: (dict) object with REQUIRED_INFO, when missing key(s), user will be asked for input.
            -start_when: (str) in the format of "YYYY-mm-dd_HH:MM"
        """
        REQUIRED_INFO = {   "NEXT_MONTH": True,         # True: next month // False: this month
                    "DATE"      : "23",         # Date-day
                    "TIME"      : "17:30",      # time: 17:00/17:30/18:00/18:30/19:00
                    "USER_NAME" : "0912345678", # user name
                    "PASSWORDS" : "abc12345",   # password
                    "PEOPLE"    : "2",          # reservation seat(s)
                    "CITY"      : "新竹市"      # restuarant location
                }
        INFO = None
        URL = "https://www.feastogether.com.tw/booking/1"

        def __init__(self, INFO:dict={}, start_when=False):
            self.luancher(INFO, start_when)

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

        def run(self):
            INFO = self.INFO
            # script start
            # -----------------------------------------------------------------------------#
            # open webpage
            driver = DriverSetup()
            driver.get(self.URL)
            driver.maximize_window()

            # click pop-up notification
            sleep(0.5)
            driver.find_element_then_click(By.XPATH, "//div[@id='modal-news']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]")

            # fill-in imformation
            driver.find_element_then_click(By.ID, "select_area")
            driver.find_element_then_click(By.XPATH, "//li[text()='"+INFO["CITY"]+"']")
            driver.find_element(By.ID, "book_people").send_keys(INFO["PEOPLE"])
            driver.find_element_then_click(By.XPATH, "//input[contains(@class,'flatpickr flatpickr-input')]")
            sleep(0.5)
            if INFO["NEXT_MONTH"]:
                driver.find_element_then_click(By.CLASS_NAME, "flatpickr-next-month")
            sleep(0.5)
            driver.find_element_then_click(By.XPATH, "(//span[text()='"+INFO["DATE"]+"'])[2]")
            driver.find_element_then_click(By.CLASS_NAME, "wk-type-dinner")

            # bottom choose store
            driver.send_ScrollDown()
            driver.send_ScrollDown()
            driver.find_element_then_click(By.XPATH, "//span[@class='cell-store']")

            # log-in
            sleep(0.5)
            driver.find_element(By.XPATH, "(//input[@placeholder='手機'])[3]").send_keys(INFO["USER_NAME"])
            driver.find_element(By.XPATH, "(//input[@type='password'])[3]").send_keys(INFO["PASSWORDS"])
            driver.find_element_then_click(By.NAME, "login")
            sleep(0.5)

            # for the warning window (change password notification)
            try:
                driver.send_Enter(driver)
            except:
                pass

            sleep(0.5)

            # bottom choose store
            driver.find_element_then_click(By.XPATH, "//span[@class='cell-store']")

            # choose reservation time
            order_time_element = driver.find_element(By.ID, "order_time")
            Select(order_time_element).select_by_visible_text(INFO["TIME"])

            # final: send_reservation
            sleep(0.5)
            driver.send_ScrollDown(4)
            sleep(0.5)
            driver.find_element_then_click(By.XPATH, "//button[@type='button']", loop_max=30)
            driver.endDriver()
        
    class Tea6(Scripts_default):
        """
            茶六
                    tested on chrome v.100 / at 2022.05.25
        Auto run with set scripts.
        :args:
            -INFO: (dict) object with REQUIRED_INFO, when missing key(s), user will be asked for input.
            -start_when: (str) in the format of "YYYY-mm-dd_HH:MM"
        """
        INFO = None
        BRANCH_URL =   {   "公益店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-LUYUEIOYwa7GCUpAFWA",
                                "朝富店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-L93VSXuz8o86ahWDRg1",
                                "中清店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-MNhWoTy962xAuCH9tCh"
                            }

        REQUIRED_INFO =  {  "DATE"      : "2022-06-22",
                            "TIME"      : "11-45",
                            "NAME"      : "金城武",
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

            # final
            driver.find_element_then_click(By.XPATH, "(//label[@class='sc-bqiRlB fCuXci'])[2]")
            driver.find_element_then_click(By.XPATH, "//button[@class='sc-ieecCq eZhyRr']")

            driver.endDriver()

    class SyaBuYo(Scripts_default):
        """
            涮乃葉
                    tested on chrome v.100 / at 2022.05.25
        Auto run with set scripts.
        :args:
            -INFO: (dict) object with REQUIRED_INFO, when missing key(s), user will be asked for input.
            -start_when: (str) in the format of "YYYY-mm-dd_HH:MM"
        """
        INFO = None
        BRANCH_URL =   {   "新竹SOGO巨城店": "https://inline.app/booking/-LPimPrzunBVFBi0ckJB:inline-live-2a466/-LPjWTrlZSINZUYENhhS", 
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

    class MoMoParadise(Scripts_default):
        """
            Mo-Mo Paradise
                    tested on chrome v.100 / at 2022.05.25
        Auto run with set scripts.
        :args:
            -INFO: (dict) object with REQUIRED_INFO, when missing key(s), user will be asked for input.
            -start_when: (str) in the format of "YYYY-mm-dd_HH:MM"
        """
        INFO = None
        BRANCH_URL =   {   "新竹巨城牧場": "https://inline.app/booking/-KlcGro3QpVV0OQ_gRcI:inline-live-humaxasia/-LHHPxqdZqtKMq-y25le", 
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
            # click purpose
            driver.find_element_then_click(By.XPATH, "//div[@value='朋友聚餐']")

            # final
            driver.find_element_then_click(By.XPATH, "(//label[@class='sc-bqiRlB fCuXci'])[2]")
            driver.find_element_then_click(By.XPATH, "//button[@class='sc-ieecCq eZhyRr']")

            driver.endDriver()