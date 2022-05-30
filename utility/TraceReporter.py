# ----------------------------------------------------------------------------------- #
# Simple TraceReporter class
# ----------------------------------------------------------------------------------- #
from datetime import datetime
class TraceReporter:
    def __init__(self, debug_flag:bool=False):
        self.report = ''
        self.debug_flag = debug_flag

    def session_start(self, text:str, level:int, end=''):
        if self.debug_flag:
            time = datetime.now().strftime('[%H:%M:%S]')
            msg = time + '\t' * level +  ' - ' + text + ' '
            print(msg, end=end)
            self.report = self.report + msg + end
            self.dump()
        

    def session_end(self, msg:str='...done'):
        if self.debug_flag:
            print(msg)
            self.report = self.report + msg + '\n'
            self.dump()

    def session_statement(self, text:str):
        if self.debug_flag:
            msg = text 
            self.report = self.report + msg
            self.dump()

    def dump(self):
        with open('TraceReporter.txt', mode='w') as f:
            f.write(self.report)