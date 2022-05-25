from TimeControl import TimeControl
# -----------------------------------------------------------------------------#
# default scripts luancher
# -----------------------------------------------------------------------------#
from time import time
class Scripts_default:
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
            self.run()

        # For multiple reservation time:
        elif isinstance(INFO["TIME"], list):
            TIME_LIST = INFO["TIME"]
            for i in range(len(TIME_LIST)):
                INFO["TIME"] = TIME_LIST[i]
                try:
                    self.run()
                    return
                except:
                    continue
        
        elapse = time() - tic
        print("elapse time: ", elapse, ' (sec.)')