from utility.Logger import Logger
from ..template import Scripts_default
from utility.DriverSetup import *

class template_FeastTogether(Scripts_default):
    def start(self):
        # -----------------------------------------------------------------------------#
        # sessions
        # -----------------------------------------------------------------------------#
        def open_webpage():
            self.log.session_start('get webpage', 1)        
            driver.get(self.URL)
            driver.maximize_window()
            self.log.session_end()            

        def click_pop_up_notification():
            # click pop-up notification
            sleep(0.5)
            self.log.session_start('click notification', 2)
            driver.find_element_then_click(By.XPATH, "//div[@id='modal-news']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]")
            self.log.session_end()

        def fill_information():
            # fill-in information
            self.log.session_start('fill area/city/people', 2)
            driver.find_element_then_click(By.ID, "select_area")
            driver.find_element_then_click(By.XPATH, "//li[text()='"+INFO["CITY"]+"']")
            driver.find_element(By.ID, "book_people").send_keys(INFO["PEOPLE"])
            self.log.session_end()

        def click_calender():
            # calender
            self.log.session_start('click calender', 2)
            driver.find_element_then_click(By.XPATH, "//input[contains(@class,'flatpickr flatpickr-input')]")
            self.log.session_end()
            sleep(0.5)
            # month        
            self.log.session_start('click month/date', 2)
            if INFO["NEXT_MONTH"]:
                driver.find_element_then_click(By.CLASS_NAME, "flatpickr-next-month")
            sleep(0.5)
            # date
            driver.find_element_then_click(By.XPATH, "(//span[text()='"+INFO["DATE"]+"'])[2]")
            self.log.session_end()

        def select_meal_time():
            # meal-time
            self.log.session_start('select meal time', 2)
            if INFO['MEALTIME'] == "晚餐":
                driver.find_element_then_click(By.CLASS_NAME, "wk-type-dinner")
            elif INFO['MEALTIME'] == "午餐":
                driver.find_element_then_click(By.XPATH, "//li[@data-mealtime='lunch']")
            elif INFO['MEALTIME'] == "下午餐":
                driver.find_element_then_click(By.XPATH, "//li[@data-mealtime='afternoon-tea']")
            self.log.session_end()

        def choose_store():
            # bottom choose store
            driver.send_ScrollDown()
            self.log.session_start('select branch-store', 2)
            response = driver.find_element_then_click(By.XPATH, "//span[text()='"+self.INFO['BRANCH']+"']")
            self.log.session_end()
            return response   
        
        def fill_login_info():
            self.log.session_start('fill log-in info', 1, '\n')
            # log-in
            sleep(0.5)
            self.log.session_start('fill username/password', 2)
            driver.find_element(By.XPATH, "(//input[@placeholder='手機'])[3]").send_keys(INFO["USER_NAME"])        
            driver.find_element(By.XPATH, "(//input[@type='password'])[3]").send_keys(INFO["PASSWORDS"])
            self.log.session_end()
            self.log.session_start('click login', 2)
            driver.find_element_then_click(By.NAME, "login")
            self.log.session_end()
            sleep(0.5)

            # for the warning window (change password notification)
            try:
                self.log.session_start('send ENTER for pop-up notification', 3)
                driver.send_Enter()
                self.log.session_end()
            except:
                pass

            sleep(0.5)       

        def choose_store():
            # bottom choose store
            driver.send_ScrollDown()
            self.log.session_start('select branch-store', 2)
            response = driver.find_element_then_click(By.XPATH, "//span[text()='"+self.INFO['BRANCH']+"']")
            self.log.session_end()
            return response   
            
        def fill_reservation_time():
            # choose reservation time
            self.log.session_start('fill reservation time', 2)
            order_time_element = driver.find_element(By.ID, "order_time")        
            Select(order_time_element).select_by_visible_text(INFO["TIME"])
            self.log.session_end()

        def send_reservation():
            # final: send_reservation        
            sleep(0.5)
            driver.send_ScrollDown(4)
            sleep(0.5)
            self.log.session_start('send_reservation', 1)
            driver.find_element_then_click(By.XPATH, "//button[@type='button']", loop_max=30)
            self.log.session_end()

        # -----------------------------------------------------------------------------#
        # execute sessions
        # -----------------------------------------------------------------------------#
        INFO = self.INFO
        driver = DriverSetup()

        open_webpage()

        click_pop_up_notification()

        self.log.session_start('fill information', 1, '\n')

        fill_information()

        click_calender()

        select_meal_time()

        if not choose_store():
            driver.save_screenshot(self.__class__.__name__+self.now()+'click_time_error.png')
            sleep(0.5)
            if not choose_store():
                self.not_available(driver)
                return False

        fill_login_info()

        if not choose_store():
            driver.save_screenshot(self.__class__.__name__+self.now()+'click_time_error.png')
            sleep(0.5)
            if not choose_store():
                self.not_available(driver)
                return False

        fill_reservation_time()

        send_reservation()

        sleep(2)
        driver.save_screenshot(self.__class__.__name__+self.now()+'_final.png')
        driver.endDriver()

        return True


    def not_available(self, driver:DriverSetup):
        print("current time (" + self.INFO['TIME'] + ") or branch-store (" + self.INFO['BRANCH'] + ") is not available.")
        print("session end.")
        driver.endDriver(wait=1)