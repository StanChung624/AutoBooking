# -----------------------------------------------------------------------------#
# default scripts __init__ and luancher
# -----------------------------------------------------------------------------#
from utility.TimeControl import TimeControl
from utility.Logger import Logger
from time import time
import json

class Scripts_default:

    def __init__(self):
        self.INFO = None
        pass

    def run(self, INFO:dict={}, start_when=False):
        if self.INFO is not None:
            INFO = self.INFO
        
        self.luancher(INFO, start_when)

    def luancher(self, INFO, start_when):
        # recorder
        rd = Logger(file_name=self.__class__.__name__, debug_flag=True)
        rd.session_start(self.__class__.__name__+' start', 0, '\n')

        # INFO checked
        self.INFO = INFO
        self.check_data()
        rd.print_INFO(INFO)

        # wait until given start_when
        if start_when:
            rd.session_start('wait until '+start_when, 0)
            TimeControl.start_when(start_when)
            rd.session_end()

        # timer - start
        tic = time()

        # For single reservation time:        
        if isinstance(INFO["TIME"], str):
            rd.session_start('run on single reservation time = '+INFO["TIME"],1, '\n')
            self.start(rd=rd)

        # For multiple reservation time:
        elif isinstance(INFO["TIME"], list):
            rd.session_start('run on multiple reservation time' ,1, '\n')
            TIME_LIST = INFO["TIME"]
            for i in range(len(TIME_LIST)):
                INFO["TIME"] = TIME_LIST[i]
                rd.session_start('time = '+INFO["TIME"] ,1, '\n')
                try:
                    self.start(rd=rd)
                    return
                except:
                    continue
        
        elapse = time() - tic
        print("elapse time: ", elapse, ' (sec.)')
        rd.session_start("elapse time: " + "{:10.4f}".format(elapse) + ' (sec.)', 0, '\n')

    def dump_required_info(self):
        with open('REQUIRED_INFO.txt', mode='w', encoding='big5') as f:
            json.dump(self.REQUIRED_INFO,f,ensure_ascii=False)

    def read_info(self):
        with open('REQUIRED_INFO.txt', mode='r', encoding='big5') as f:
            self.INFO = json.load(f)
        print(self.INFO)
    