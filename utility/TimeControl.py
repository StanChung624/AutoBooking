from time import sleep
from datetime import datetime
import pandas as pd

class TimeControl_printer:
    def __init__(self):        
        self.called = 0
        self.length = 0
    def print_wait(self, start_time):
        current_time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        self.called += 1
        if self.called == 1:
            self.length = len(current_time+' >> wait until >> '+start_time)
            print(current_time+' >> wait until >>'+start_time, end='')
        elif self.called > 1:
            print(self.length * "\r" + current_time+' >> wait until >> '+start_time, end='')

class TimeControl:
    def start_when(start_time):
        """
        Continue when start_time is passed.
        (start_time) in the format of : %Y-%m-%d_%H:%M
        
        :Usage:
            ::
                TimeControl.start_when("2022-06-24_09:00")
        """
        proceed =  datetime.now() > pd.to_datetime(start_time, format='%Y-%m-%d_%H:%M')
        printer = TimeControl_printer()
        printer.print_wait(start_time)        

        while not proceed:
            proceed =  datetime.now() > pd.to_datetime(start_time, format='%Y-%m-%d_%H:%M')            
            if proceed:
                pass
            else:
                printer.print_wait(start_time)
                sleep(1)
        print('\n<start>')
