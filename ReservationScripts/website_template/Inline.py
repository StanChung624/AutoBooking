from utility.Logger import Logger
from ..template import Scripts_default
from utility.DriverSetup import *
from time import sleep

class template_Inline(Scripts_default):

    def start(self, rd:Logger):
        INFO = self.INFO
        # script start
        # -----------------------------------------------------------------------------#
        # open webpage
        rd.session_start('get webpage', 1)
        driver = DriverSetup()        
        driver.get(self.BRANCH_URL[INFO["BRANCH"]])
        driver.maximize_window()
        rd.session_end()

        sleep(0.5)

        rd.session_start('fill information', 1, '\n')
        # fill-in people
        rd.session_start('select people', 2)
        element = driver.find_element(By.XPATH, "//select[@class='sc-dJjYzT kxiniR']")
        Select(element).select_by_index(int(INFO['PEOPLE']))
        rd.session_end()
        # fill-in date
        rd.session_start('click calender', 2)
        driver.find_element_then_click(By.XPATH, "//div[@class='sc-dJjYzT kxiniR']")
        rd.session_end()
        driver.send_ScrollDown()

        # if DATE is unavailable
        rd.session_start('click date', 2)
        response = driver.find_element_then_click(By.XPATH, "//div[@data-date='"+INFO["DATE"]+"']//span[1]")
        if not response:
            rd.session_start('info date is not available', 1, '\n')
            self.not_available(driver)
            return
        rd.session_end()
        # if TIME is unavailable
        rd.session_start('click time', 2)
        response = driver.find_element_then_click(By.XPATH, "//button[@data-cy='book-now-time-slot-box-"+INFO["TIME"]+"']")
        if not response:
            rd.session_start('info date is not available', 1, '\n')
            self.not_available(driver)
            return
        rd.session_end()

        rd.session_start('click next step', 1, '\n')
        # fill-in user info
        driver.find_element_then_click(By.XPATH, "//span[text()='下一步，填寫聯絡資訊']")
        sleep(0.5)
        rd.session_start('fill name', 2)
        driver.find_element(By.ID, "name").send_keys(INFO["NAME"])
        rd.session_end()
        rd.session_start('fill phone number', 2)
        driver.find_element(By.ID, "phone").send_keys(INFO["PHONE"])
        rd.session_end()
        rd.session_start('click dining purpose', 2)
        driver.find_element_then_click(By.XPATH, "//div[@value='朋友聚餐']")
        rd.session_end()

        # final
        rd.session_start('final step',1, '\n')
        rd.session_start('check box', 2)
        driver.find_element_then_click(By.XPATH, "(//label[@class='sc-bqiRlB fCuXci'])[2]")
        rd.session_end()
        rd.session_start('send reservation request', 2)
        driver.find_element_then_click(By.XPATH, "//button[@class='sc-ieecCq eZhyRr']")
        rd.session_end()

        driver.endDriver()

    def not_available(self, driver:DriverSetup):
        print("current date ("+ self.INFO['DATE'] +"), time (" + self.INFO['TIME'] + ") or branch-store (" + self.INFO['BRANCH'] + ") is not available.")
        print("session end.")
        driver.quit()