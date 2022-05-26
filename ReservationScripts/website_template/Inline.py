from ..template import Scripts_default
from DriverSetup import *
from time import sleep

class template_Inline(Scripts_default):

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