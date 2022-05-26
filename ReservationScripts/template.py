# -----------------------------------------------------------------------------#
# default scripts __init__ and luancher
# -----------------------------------------------------------------------------#
from TimeControl import TimeControl
from time import time
class Scripts_default:

    def __init__(self):
        pass

    def run(self, INFO:dict={}, start_when=False):
        self.luancher(INFO, start_when)

    def luancher(self, INFO, start_when):
        # INFO checked
        self.INFO = INFO
        self.check_data()

        # wait until given start_when
        if start_when:
            TimeControl.start_when(start_when)

        # timer - start
        tic = time()

        # For single reservation time:        
        if isinstance(INFO["TIME"], str):
            self.start()

        # For multiple reservation time:
        elif isinstance(INFO["TIME"], list):
            TIME_LIST = INFO["TIME"]
            for i in range(len(TIME_LIST)):
                INFO["TIME"] = TIME_LIST[i]
                try:
                    self.start()
                    return
                except:
                    continue
        
        elapse = time() - tic
        print("elapse time: ", elapse, ' (sec.)')

    def dump_required_info(self):
        print(self.REQUIRED_INFO)