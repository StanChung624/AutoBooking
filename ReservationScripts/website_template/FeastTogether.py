from utility.Logger import Logger
from ..template import Scripts_default
from utility.DriverSetup import *

class template_FeastTogether(Scripts_default):
    def start(self, rd:Logger):
        INFO = self.INFO
        # script start
        # -----------------------------------------------------------------------------#
        # open webpage
        rd.session_start('get webpage', 1)
        driver = DriverSetup()
        driver.get(self.URL)
        driver.maximize_window()
        rd.session_end()

        # click pop-up notification
        sleep(0.5)
        rd.session_start('click notification', 2)
        driver.find_element_then_click(By.XPATH, "//div[@id='modal-news']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]")
        rd.session_end()

        rd.session_start('fill information', 1, '\n')
        # fill-in information
        rd.session_start('fill area/city/people', 2)
        driver.find_element_then_click(By.ID, "select_area")
        driver.find_element_then_click(By.XPATH, "//li[text()='"+INFO["CITY"]+"']")
        driver.find_element(By.ID, "book_people").send_keys(INFO["PEOPLE"])
        rd.session_end()
        # calender
        rd.session_start('click calender', 2)
        driver.find_element_then_click(By.XPATH, "//input[contains(@class,'flatpickr flatpickr-input')]")
        rd.session_end()
        sleep(0.5)
        # month        
        rd.session_start('click month/date', 2)
        if INFO["NEXT_MONTH"]:
            driver.find_element_then_click(By.CLASS_NAME, "flatpickr-next-month")
        sleep(0.5)
        # date
        driver.find_element_then_click(By.XPATH, "(//span[text()='"+INFO["DATE"]+"'])[2]")
        rd.session_end()

        # meal-time
        rd.session_start('select meal time', 2)
        if INFO['MEALTIME'] == "晚餐":
            driver.find_element_then_click(By.CLASS_NAME, "wk-type-dinner")
        elif INFO['MEALTIME'] == "午餐":
            driver.find_element_then_click(By.XPATH, "//li[@data-mealtime='lunch']")
        elif INFO['MEALTIME'] == "下午餐":
            driver.find_element_then_click(By.XPATH, "//li[@data-mealtime='afternoon-tea']")
        rd.session_end()

        # bottom choose store
        driver.send_ScrollDown()
        rd.session_start('select branch-store', 2)
        response = driver.find_element_then_click(By.XPATH, "//span[text()='"+self.INFO['BRANCH']+"']")
        rd.session_end()
        if not response:
            rd.session_start('info time is not available', 1, '\n')
            self.not_available(driver)
            return
        
        rd.session_start('fill log-in info', 1, '\n')
        # log-in
        sleep(0.5)
        rd.session_start('fill username/password', 2)
        driver.find_element(By.XPATH, "(//input[@placeholder='手機'])[3]").send_keys(INFO["USER_NAME"])        
        driver.find_element(By.XPATH, "(//input[@type='password'])[3]").send_keys(INFO["PASSWORDS"])
        rd.session_end()
        rd.session_start('click login', 2)
        driver.find_element_then_click(By.NAME, "login")
        rd.session_end()
        sleep(0.5)

        # for the warning window (change password notification)
        try:
            rd.session_start('send ENTER for pop-up notification', 3)
            driver.send_Enter(driver)
            rd.session_end()
        except:
            pass

        sleep(0.5)

        # bottom choose store
        rd.session_start('select branch-store', 2)
        response = driver.find_element_then_click(By.XPATH, "//span[text()='"+self.INFO['BRANCH']+"']")
        rd.session_end()
        if not response:
            rd.session_start('info time is not available', 1, '\n')
            self.not_available(driver)
            return        
            
        # choose reservation time
        rd.session_start('fill reservation time', 2)
        order_time_element = driver.find_element(By.ID, "order_time")        
        Select(order_time_element).select_by_visible_text(INFO["TIME"])
        rd.session_end()

        # final: send_reservation        
        sleep(0.5)
        driver.send_ScrollDown(4)
        sleep(0.5)
        rd.session_start('send_reservation', 1)
        driver.find_element_then_click(By.XPATH, "//button[@type='button']", loop_max=30)
        rd.session_end()
        driver.endDriver()

    def not_available(self, driver:DriverSetup):
        print("current time (" + self.INFO['TIME'] + ") or branch-store (" + self.INFO['BRANCH'] + ") is not available.")
        print("session end.")
        input()
        driver.quit()