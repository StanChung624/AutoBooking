# ----------------------------------------------------------------------------------- #
# Simple TraceReporter class
# ----------------------------------------------------------------------------------- #
from datetime import datetime
class Logger:
    def __init__(self, file_name:str='Reporter', debug_flag:bool=True):
        self.report = ''
        self.file_name = file_name + '_report'
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

    def print_INFO(self, INFO:dict):
        if self.debug_flag:
            msg = 'start of INFO\n'
            for key in INFO.keys():
                msg = msg + '\t' + key + ' = ' + str(INFO[key]) + '\n'
            msg = msg + 'end of INFO\n'
            print(msg)
            self.report = self.report + msg
            self.dump()

    def dump(self):
        with open(self.file_name+'.txt', mode='w') as f:
            f.write(self.report)

    