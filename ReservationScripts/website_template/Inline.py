from utility.Logger import Logger
from ..template import Scripts_default
from utility.DriverSetup import *
from time import sleep

class template_Inline(Scripts_default):
    
    def start(self):
        # -----------------------------------------------------------------------------#
        # sessions
        # -----------------------------------------------------------------------------#
        def get_webpage():
            self.log.session_start('get webpage', 1)                   
            driver.get(self.URL)
            driver.maximize_window()
            self.log.session_end()            

        def fill_people():
            self.log.session_start('select people', 2)
            element = driver.wait_find_element(By.XPATH, "//select[@class='sc-dJjYzT kxiniR']")
            Select(element).select_by_index(int(INFO['PEOPLE']))
            self.log.session_end()

        def click_calender():
            self.log.session_start('click calender', 2)
            driver.find_element_then_click(By.XPATH, "//div[@class='sc-dJjYzT kxiniR']")
            self.log.session_end()
            driver.send_ScrollDown()

        def click_date():
            self.log.session_start('click date', 2)
            response = driver.find_element_then_click(By.XPATH, "//div[@data-date='"+INFO["DATE"]+"']//span[1]")
            if not response:
                self.log.session_start('info DATE is not available', 1, '\n')            
                return False
            else:                
                self.log.session_end()
                return True
        
        def click_time():
            self.log.session_start('click time', 2)
            response = driver.find_element_then_click(By.XPATH, "//button[@data-cy='book-now-time-slot-box-"+INFO["TIME"]+"']")
            if not response:
                self.log.session_start('info TIME is not available', 1, '\n')            
                return False
            else:                
                self.log.session_end()
                return True

        def click_next_step():
            # fill-in user info
            driver.find_element_then_click(By.XPATH, "//span[text()='下一步，填寫聯絡資訊']")
            sleep(0.5)
            self.log.session_start('click dining purpose', 2)
            driver.find_element_then_click(By.XPATH, "//div[@value='朋友聚餐']")
            self.log.session_start('fill name', 2)
            driver.find_element(By.ID, "name").send_keys(INFO["NAME"])
            self.log.session_start('fill phone number', 2)
            driver.find_element(By.ID, "phone").send_keys(INFO["PHONE"])
            self.log.session_end()

        def final_check_box_and_send():
            # final
            self.log.title('final step',1)
            self.log.session_start('check box', 2)
            driver.find_element_then_click(By.XPATH, "(//label[@class='sc-bqiRlB fCuXci'])[2]")
            self.log.session_end()
            self.log.session_start('send reservation request', 2)
            driver.find_element_then_click(By.XPATH, "//button[@class='sc-ieecCq eZhyRr']")
            self.log.session_end()

        # -----------------------------------------------------------------------------#
        # execute sessions
        # -----------------------------------------------------------------------------#
        INFO = self.INFO
        driver = DriverSetup() 

        get_webpage()

        fill_people()

        click_calender()

        is_click_date_succeeded = click_date()

        if not is_click_date_succeeded:
            driver.save_screenshot(self.__class__.__name__+self.now()+'click_date_error.png')
            self.not_available(driver)
            return False
        
        is_click_time_succeeded = click_time()

        if not is_click_time_succeeded:
            driver.save_screenshot(self.__class__.__name__+self.now()+'click_time_error.png')
            self.not_available(driver)
            return False

        click_next_step()

        final_check_box_and_send()

        sleep(1)
        driver.save_screenshot('screenshot\\'+self.now()+'_final.png')
        driver.endDriver()
        
        return True

    # -----------------------------------------------------------------------------#
    # error response
    # -----------------------------------------------------------------------------#
    def not_available(self, driver:DriverSetup):
        print("current date ("+ self.INFO['DATE'] +"), time (" + self.INFO['TIME'] + ") or branch-store is not available.")
        print("session end.")
        driver.endDriver(wait=1)
        
    