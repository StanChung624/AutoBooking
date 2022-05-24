from DriverSetup import *
class Scripts:
    # -----------------------------------------------------------------------------#
    #       饗食天堂
    # -----------------------------------------------------------------------------#
    class Paradise():
        INFO = None
        def __init__(self, INFO):
            # For single reservation time:
            self.INFO = INFO
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
                    
        def run(self):
            INFO = self.INFO
            # script start
            # -----------------------------------------------------------------------------#
            # open webpage
            driver = DriverSetup()
            driver.get('https://www.feastogether.com.tw/booking/01')
            driver.maximize_window()

            # click pop-up notification
            sleep(1)
            driver.find_element_then_click(DriverUtility.By.XPATH, "//div[@id='modal-news']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]")

            # fill-in imformation
            driver.find_element_then_click(DriverUtility.By.ID, "select_area")
            driver.find_element_then_click(DriverUtility.By.XPATH, "//li[text()='"+INFO["CITY"]+"']")
            driver.find_element(DriverUtility.By.ID, "book_people").send_keys(INFO["PEOPLE"])
            driver.find_element_then_click(DriverUtility.By.XPATH, "//input[contains(@class,'flatpickr flatpickr-input')]")
            sleep(0.5)
            if INFO["NEXT_MONTH"]:
                driver.find_element_then_click(DriverUtility.By.CLASS_NAME, "flatpickr-next-month")
            sleep(0.5)
            driver.find_element_then_click(DriverUtility.By.XPATH, "(//span[text()='"+INFO["DATE"]+"'])[2]")
            driver.find_element_then_click(DriverUtility.By.CLASS_NAME, "wk-type-dinner")

            # bottom choose store
            driver.send_ScrollDown()
            driver.send_ScrollDown()
            driver.loop_for_element_click(DriverUtility.By.XPATH, "//tr[@class='wk-book-stores list-tr']//td[1]")

            # log-in
            sleep(0.5)
            driver.find_element(DriverUtility.By.XPATH, "(//input[@placeholder='手機'])[3]").send_keys(INFO["USER_NAME"])
            driver.find_element(DriverUtility.By.XPATH, "(//input[@type='password'])[3]").send_keys(INFO["PASSWORDS"])
            driver.find_element_then_click(DriverUtility.By.NAME, "login")
            sleep(0.5)

            # for the warning window (change password notification)
            try:
                driver.send_Enter(driver)
            except:
                pass

            sleep(0.5)

            # bottom choose store
            driver.loop_for_element_click(DriverUtility.By.XPATH, "//tr[@class='wk-book-stores list-tr']//td[1]")

            # choose reservation time
            order_time_element = driver.find_element(DriverUtility.By.ID, "order_time")
            DriverUtility.Select(order_time_element).select_by_visible_text(INFO["TIME"])

            # final: send_reservation
            sleep(0.5)
            driver.send_ScrollDown(4)
            sleep(0.5)
            driver.loop_for_element_click(DriverUtility.By.XPATH, "//button[@type='button']")
            driver.endDriver()

    # -----------------------------------------------------------------------------#
    #       旭集
    # -----------------------------------------------------------------------------#
    class Sunrise():
        INFO = None
        def __init__(self, INFO):
            # For single reservation time:
            self.INFO = INFO
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
            
        def run(self):
            INFO = self.INFO
            # script start
            # -----------------------------------------------------------------------------#
            # open webpage
            driver = DriverSetup()
            driver.get('https://www.feastogether.com.tw/booking/10')
            driver.maximize_window()

            # click pop-up notification
            sleep(0.5)
            driver.find_element_then_click(DriverUtility.By.XPATH, "//div[@id='modal-news']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]")

            # fill-in imformation
            driver.find_element_then_click(DriverUtility.By.ID, "select_area")
            driver.find_element_then_click(DriverUtility.By.XPATH, "//li[text()='"+INFO["CITY"]+"']")
            driver.find_element(DriverUtility.By.ID, "book_people").send_keys(INFO["PEOPLE"])
            driver.find_element_then_click(DriverUtility.By.XPATH, "//input[contains(@class,'flatpickr flatpickr-input')]")
            sleep(0.5)
            if INFO["NEXT_MONTH"]:
                driver.find_element_then_click(DriverUtility.By.CLASS_NAME, "flatpickr-next-month")
            sleep(0.5)
            driver.find_element_then_click(DriverUtility.By.XPATH, "(//span[text()='"+INFO["DATE"]+"'])[2]")
            driver.find_element_then_click(DriverUtility.By.CLASS_NAME, "wk-type-dinner")

            # bottom choose store
            driver.send_ScrollDown()
            driver.send_ScrollDown()
            driver.loop_for_element_click(DriverUtility.By.XPATH, "//tr[@class='wk-book-stores list-tr']//td[1]")

            # log-in
            sleep(0.5)
            driver.find_element(DriverUtility.By.XPATH, "(//input[@placeholder='手機'])[3]").send_keys(INFO["USER_NAME"])
            driver.find_element(DriverUtility.By.XPATH, "(//input[@type='password'])[3]").send_keys(INFO["PASSWORDS"])
            driver.find_element_then_click(DriverUtility.By.NAME, "login")
            sleep(0.5)

            # for the warning window (change password notification)
            try:
                driver.send_Enter(driver)
            except:
                pass

            sleep(0.5)

            # bottom choose store
            driver.loop_for_element_click(DriverUtility.By.XPATH, "//tr[@class='wk-book-stores list-tr']//td[1]")

            # choose reservation time
            order_time_element = driver.find_element(DriverUtility.By.ID, "order_time")
            DriverUtility.Select(order_time_element).select_by_visible_text(INFO["TIME"])

            # final: send_reservation
            sleep(0.5)
            driver.send_ScrollDown(4)
            sleep(0.5)
            driver.loop_for_element_click(DriverUtility.By.XPATH, "//button[@type='button']", loop_max=30)
            driver.endDriver()

    # -----------------------------------------------------------------------------#
    #       茶六
    # -----------------------------------------------------------------------------#
    class Tea6():
        INFO = None
        def __init__(self, INFO:dict):
            # For single reservation time:
            self.INFO = INFO
            if isinstance(INFO.TIME, str):
                self.run()
            # For multiple reservation time:
            elif isinstance(INFO.TIME, list):
                TIME_LIST = INFO.TIME
                for i in range(len(TIME_LIST)):
                    INFO.TIME = TIME_LIST[i]
                    try:
                        self.run()
                        return
                    except:
                        continue
            
        def run(self):
            INFO = self.INFO
            # script start
            # -----------------------------------------------------------------------------#
            # open webpage
            driver = DriverSetup()
            Tea6_branch_url = {"公益店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-LUYUEIOYwa7GCUpAFWA",
                            "朝富店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-L93VSXuz8o86ahWDRg1",
                            "中清店": "https://inline.app/booking/-L93VSXuz8o86ahWDRg0:inline-live-karuizawa/-MNhWoTy962xAuCH9tCh"}
            driver.get(Tea6_branch_url[INFO["BRANCH"]])
            sleep(0.5)
            driver.maximize_window()

            # fill-in date
            driver.find_element_then_click(By.XPATH, "//div[@class='sc-dJjYzT kxiniR']")
            driver.send_ScrollDown()
            driver.loop_for_element_click(By.XPATH, "//div[@data-date='"+INFO["DATE"]+"']//span[1]")
            driver.loop_for_element_click(By.XPATH, "//button[@data-cy='book-now-time-slot-box-"+INFO["TIME"]+"']")

            # fill-in user info
            driver.find_element_then_click(By.XPATH, "//span[text()='下一步，填寫聯絡資訊']")
            sleep(0.5)
            driver.find_element(By.ID, "name").send_keys(INFO["NAME"])
            driver.find_element(By.ID, "phone").send_keys(INFO["PHONE"])

            # final
            driver.find_element_then_click(By.XPATH, "(//label[@class='sc-bqiRlB fCuXci'])[2]")
            driver.find_element_then_click(By.XPATH, "//button[@class='sc-ieecCq eZhyRr']")

            driver.endDriver()