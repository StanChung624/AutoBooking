from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

from setuptools import find_namespace_packages

#### importing class "By" and "Select" ####
class DriverUtility():
    class By(By):
        pass
        
    class Select(Select):
        pass

#### DriverSetup ####
class DriverSetup(Chrome):
    """
        Return a driver for further webpage operation.

        :Usage:
            ::
                driver = DriverSetup()

        :rtype: WebElement
    """
    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self = super().__init__(options=options)

    def endDriver(self):
        print('*'*51)
        print('** Auto fill-in completed. Press Enter to Exit...**')    
        input('*'*51+'\n')

    def monthDays(self, startYYYmm):
        startYYY = startYYYmm[:3]
        startmm = startYYYmm[3:]
        if startYYY in ['113','117','121']:
            days = {['01','03','05','07','08','10','12']:'31',
                    ['04','06','09','11']:'30',
                    '02':'29'}
        else:
            days = {['01','03','05','07','08','10','12']:'31',
                    ['04','06','09','11']:'30',
                    '02':'28'}
        if int(startmm) == 12:
            endYYY = str(int(startYYY)+1)
            endmm = '01'
        else:
            endYYY = startYYY
            endmm = str(int(startmm)) + 1
        if len(endmm) == 1:
            endmm = '0' + endmm

        return [endYYY, endmm, days[endmm]]

    def send_ScrollDown(self, times:int=1):
        for i in range(times):
            body = self.find_element_by_css_selector('body')
            body.send_keys(Keys.PAGE_DOWN)

    def send_End(self):
        body = self.find_element_by_css_selector('body')
        body.send_keys(Keys.END)

    def send_Enter(self):
        body = self.find_element_by_css_selector('body')
        body.send_keys(Keys.ENTER)

    def loop_for_element_click(self, by:By, value:str, sleep_time:float = 0.5, loop_max:int = 10):
        loop_index = 0
        looper = True
        while loop_index != loop_max and looper:
            loop_index += 1
            if loop_index >= 2:
                self.send_ScrollDown()
            try:
                self.find_element(by=by, value=value).click()
                looper = False
            except:
                sleep(sleep_time)
                self.send_ScrollDown()
                self.find_element_then_click(by=by, value=value)
                looper = False
            finally:
                continue

        if looper:
            self.find_element(by=by, value=value).click()

    def find_element_then_click(self, by:By, value:str):
        try:
            element = self.find_element(by=by, value=value)
        except:
            sleep(0.5)
            element = self.find_element(by=by, value=value)
        
        try:
            element.click()
        except:
            sleep(0.5)
            element.click()
