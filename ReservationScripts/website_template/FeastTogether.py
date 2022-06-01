from utility.Logger import Logger
from ..template import Scripts_default
from utility.DriverSetup import *

class template_FeastTogether(Scripts_default):
    def start(self, log:Logger):
        INFO = self.INFO
        # script start
        # -----------------------------------------------------------------------------#
        # open webpage
        log.session_start('get webpage', 1)
        driver = DriverSetup()
        driver.get(self.URL)
        driver.maximize_window()
        log.session_end()

        # click pop-up notification
        sleep(0.5)
        log.session_start('click notification', 2)
        driver.find_element_then_click(By.XPATH, "//div[@id='modal-news']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]")
        log.session_end()

        log.session_start('fill information', 1, '\n')
        # fill-in information
        log.session_start('fill area/city/people', 2)
        driver.find_element_then_click(By.ID, "select_area")
        driver.find_element_then_click(By.XPATH, "//li[text()='"+INFO["CITY"]+"']")
        driver.find_element(By.ID, "book_people").send_keys(INFO["PEOPLE"])
        log.session_end()
        # calender
        log.session_start('click calender', 2)
        driver.find_element_then_click(By.XPATH, "//input[contains(@class,'flatpickr flatpickr-input')]")
        log.session_end()
        sleep(0.5)
        # month        
        log.session_start('click month/date', 2)
        if INFO["NEXT_MONTH"]:
            driver.find_element_then_click(By.CLASS_NAME, "flatpickr-next-month")
        sleep(0.5)
        # date
        driver.find_element_then_click(By.XPATH, "(//span[text()='"+INFO["DATE"]+"'])[2]")
        log.session_end()

        # meal-time
        log.session_start('select meal time', 2)
        if INFO['MEALTIME'] == "晚餐":
            driver.find_element_then_click(By.CLASS_NAME, "wk-type-dinner")
        elif INFO['MEALTIME'] == "午餐":
            driver.find_element_then_click(By.XPATH, "//li[@data-mealtime='lunch']")
        elif INFO['MEALTIME'] == "下午餐":
            driver.find_element_then_click(By.XPATH, "//li[@data-mealtime='afternoon-tea']")
        log.session_end()

        # bottom choose store
        driver.send_ScrollDown()
        log.session_start('select branch-store', 2)
        response = driver.find_element_then_click(By.XPATH, "//span[text()='"+self.INFO['BRANCH']+"']")
        log.session_end()
        if not response:
            log.session_start('info time is not available', 1, '\n')
            self.not_available(driver)
            return
        
        log.session_start('fill log-in info', 1, '\n')
        # log-in
        sleep(0.5)
        log.session_start('fill username/password', 2)
        driver.find_element(By.XPATH, "(//input[@placeholder='手機'])[3]").send_keys(INFO["USER_NAME"])        
        driver.find_element(By.XPATH, "(//input[@type='password'])[3]").send_keys(INFO["PASSWORDS"])
        log.session_end()
        log.session_start('click login', 2)
        driver.find_element_then_click(By.NAME, "login")
        log.session_end()
        sleep(0.5)

        # for the warning window (change password notification)
        try:
            log.session_start('send ENTER for pop-up notification', 3)
            driver.send_Enter()
            log.session_end()
        except:
            pass

        sleep(0.5)

        # bottom choose store
        log.session_start('select branch-store', 2)
        response = driver.find_element_then_click(By.XPATH, "//span[text()='"+self.INFO['BRANCH']+"']")
        log.session_end()
        if not response:
            log.session_start('info time is not available', 1, '\n')
            self.not_available(driver)
            return        
            
        # choose reservation time
        log.session_start('fill reservation time', 2)
        order_time_element = driver.find_element(By.ID, "order_time")        
        Select(order_time_element).select_by_visible_text(INFO["TIME"])
        log.session_end()

        # final: send_reservation        
        sleep(0.5)
        driver.send_ScrollDown(4)
        sleep(0.5)
        log.session_start('send_reservation', 1)
        driver.find_element_then_click(By.XPATH, "//button[@type='button']", loop_max=30)
        log.session_end()
        driver.endDriver()

    def not_available(self, driver:DriverSetup):
        print("current time (" + self.INFO['TIME'] + ") or branch-store (" + self.INFO['BRANCH'] + ") is not available.")
        print("session end.")
        driver.quit()