from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from StringProcess import setw

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

        :rtype: Driver
    """
    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self = super().__init__(options=options)

    def endDriver(self):
        end_msg = 'Driver end in 5 second...'
        for i in range(5,0,-1):
            print('Driver end in '+str(i)+' second...'+'\r'*len(end_msg),end='')
            sleep(1)
        print('')
        print('*'*51)
        print(setw('* Auto fill-in completed. *',51,'mid'))
        print('*'*51+'\n')


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

    def find_element_then_click(self, by:By, value:str, sleep_time:float = 0.5, loop_max:int = 10):
        loop_index = 0
        looper = True
        # attemp-session
        try:
            self.find_element(by=by, value=value).click()
            looper = False
        except:
            try:
                sleep(0.5)
                element = self.find_element(by=by, value=value)
                self.execute_script("arguments[0].click();", element)
                looper = False
            except:
                pass        
        # loop-session
        while loop_index != loop_max and looper:
            loop_index += 1
            if loop_index >= 2:
                self.send_ScrollDown()
            try:
                element = self.find_element(by=by, value=value)
                self.execute_script("arguments[0].click();", element)
                looper = False
            except:
                sleep(sleep_time)
                self.send_ScrollDown()
                self.find_element(by=by, value=value).click()
                looper = False
            finally:
                continue

        if looper:
            self.find_element(by=by, value=value).click()
