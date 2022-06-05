# ----------------------------------------------------------------------------------- #
# Simple Logger class
# ----------------------------------------------------------------------------------- #
from datetime import datetime
class Logger:
    def __init__(self, file_name:str='Reporter', debug_flag:bool=True):
        self.report = ''
        self.file_name = file_name + '_report'
        self.debug_flag = debug_flag
        self.is_without_session_end = False

    def title(self, text:str, level:int, end='\n'):
        if self.debug_flag:            
            msg = self.get_time() + '\t' * level + ' - ' + text + ' '
            print(msg, end=end)
            self.report = self.report + msg + end
            self.dump()
            self.is_without_session_end = False

    def session_start(self, text:str, level:int, end='', output_print:bool=True):
        if self.debug_flag:
            # auto end last session
            if self.is_without_session_end:
                msg = '...done\n'
            else:
                msg = ''
            msg = msg + self.get_time() + '\t' * level +  ' - ' + text + ' '
            if output_print:
                print(msg, end=end)
            self.report = self.report + msg + end
            self.dump()
            self.is_without_session_end = True

    def session_end(self, msg:str='...done'):
        if self.debug_flag:
            print(msg)
            self.report = self.report + msg + '\n'
            self.dump()
            self.is_without_session_end = False

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

    def get_time(self):
        return datetime.now().strftime('[%H:%M:%S]')