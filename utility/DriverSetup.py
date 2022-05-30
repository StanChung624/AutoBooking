from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from utility.StringProcess import setw

#### importing class "By" and "Select" ####
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

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
        # silence the driver output
        options.add_argument("--log-level=3")
        self = super().__init__(options=options)

    def endDriver(self, wait:float=10):        
        for i in range(wait,0,-1):
            end_msg = 'Driver end in '+str(i)+' second...'
            print( end_msg + '\r'*len(end_msg), end='')
            sleep(1)
        print('')
        print('*'*51)
        print(setw('* Auto fill-in completed. *',51,'mid'))
        print('*'*51+'\n')


    def send_ScrollDown(self, times:int=1):
        """
        Send SCROLL-DOWN to page.
        
        :args::

        -times(int) : send multiple times.
        """
        for i in range(times):
            body = self.find_element_by_css_selector('body')
            body.send_keys(Keys.PAGE_DOWN)

    def send_End(self, times:int=1):
        """
        Send END to page.
        
        :args::

        -times(int) : send multiple times.
        """
        body = self.find_element_by_css_selector('body')
        body.send_keys(Keys.END)

    def send_Enter(self):
        body = self.find_element_by_css_selector('body')
        body.send_keys(Keys.ENTER)

    def send_Left_Alt(self):
        body = self.find_element_by_css_selector('body')
        body.send_keys(Keys.ALT, Keys.LEFT)

    def send_Right_Alt(self):
        body = self.find_element_by_css_selector('body')
        body.send_keys(Keys.ALT, Keys.RIGHT)

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
                #self.send_ScrollDown()
                pass
            try:
                element = self.find_element(by=by, value=value)
                self.execute_script("arguments[0].click();", element)
                looper = False
            except:
                sleep(sleep_time)
                #self.send_ScrollDown()
                self.find_element(by=by, value=value).click()
                looper = False
            finally:
                continue

        if looper:
            return False
        else:
            return True

    def wait_clickable_then_click(self, by:By, value:str, timeout:float=5):

        method = EC.element_to_be_clickable((by, value))
        element = WebDriverWait(self, timeout=timeout).until(method=method)        
        if not element:
            self.find_element_then_click(by=by, value=value)               
            return True 
        else:
            return False
        
    def wait_find_element(self, by:By, value:str, timeout:float=7):            
        looper = True
        time = 0
        while looper:
            if time > timeout:
                break
            try:
                el = self.find_element(by=by, value=value)
                if el.is_enabled():
                    return el
                else:
                    pass
            except:
                sleep(0.5)
                time += 0.5
        raise "can't find element"

    def get_text_excluding_children(self, by:By, value:str, timeout:float=7):
        looper = True
        time = 0
        while looper:
            if time > timeout:
                break
            try:
                element = self.find_element(by=by , value=value)
                return self.execute_script("""
                                            return jQuery(arguments[0]).contents().filter(function() {
                                                return this.nodeType == Node.TEXT_NODE;
                                            }).text();
                                            """, element)
            except:
                sleep(0.5)
                time += 0.5
        element = self.find_element(by=by , value=value)
        return self.execute_script("""
        return jQuery(arguments[0]).contents().filter(function() {
            return this.nodeType == Node.TEXT_NODE;
        }).text();
        """, element)
