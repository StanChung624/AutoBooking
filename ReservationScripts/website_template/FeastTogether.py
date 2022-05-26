from ..template import Scripts_default
from DriverSetup import *

class template_FeastTogether(Scripts_default):
    def start(self):
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
        # meal-time
        if INFO['MEALTIME'] == "晚餐":
            driver.find_element_then_click(By.CLASS_NAME, "wk-type-dinner")
        elif INFO['MEALTIME'] == "午餐":
            driver.find_element_then_click(By.XPATH, "//li[@data-mealtime='lunch']")
        elif INFO['MEALTIME'] == "下午餐":
            driver.find_element_then_click(By.XPATH, "//li[@data-mealtime='afternoon-tea']")

        # bottom choose store
        driver.send_ScrollDown()
        response = driver.wait_clickable_then_click(By.XPATH, "//span[text()='"+self.INFO['BRANCH']+"']", timeout=5)
        if not response:
            self.not_available(driver)
            return
            del response

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
        response = driver.wait_clickable_then_click(By.XPATH, "//span[text()='"+self.INFO['BRANCH']+"']", timeout=5)
        if not response:
            self.not_available(driver)
            return
            del response
            
        # choose reservation time
        order_time_element = driver.find_element(By.ID, "order_time")
        Select(order_time_element).select_by_visible_text(INFO["TIME"])

        # final: send_reservation
        sleep(0.5)
        driver.send_ScrollDown(4)
        sleep(0.5)
        driver.find_element_then_click(By.XPATH, "//button[@type='button']", loop_max=30)
        driver.endDriver()

    def not_available(self, driver:DriverSetup):
        print("current time (" + self.INFO['TIME'] + ") or branch-store (" + self.INFO['BRANCH'] + ") is not available.")
        print("session end.")
        driver.quit()