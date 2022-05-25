from .template import Scripts_default
from DriverSetup import *

class Paradise(Scripts_default):
    """
        饗食天堂
                tested on chrome v.100 / at 2022.05.25
    Auto run with set scripts.
    
    Parameters
    ----------
        -INFO : dict 
            refer to REQUIRED_INFO as an example. When missing key(s), user will be asked for input.

        -start_when : str
            in the format of "YYYY-mm-dd_HH:MM"
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
    