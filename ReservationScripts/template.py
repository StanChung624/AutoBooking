# -----------------------------------------------------------------------------#
# default scripts __init__ and luancher
# -----------------------------------------------------------------------------#
from utility.TimeControl import TimeControl
from utility.Logger import Logger
from time import time
import json

class Scripts_default:
    """
    Default crawler methods.    
    """
    REQUIRED_INFO = ''
    url = ''
    # -----------------------------------------------------------------------------#
    # defualt methods
    # -----------------------------------------------------------------------------#
    def __init__(self):
        self.INFO = None
        pass

    def run(self, INFO:dict=None, start_when=False):
        """
        Start crawling process. Automatically call self.launcher for different kinds of input condition.

        Parameters:
        ---
        INFO:`dict` keys and values depend on target website.
        start_when: `str` in format of "YYYY-mm-dd_HH:MM".
        """
        if self.INFO is not None:
            INFO = self.INFO
        
        self.luancher(INFO, start_when)    

    def luancher(self, INFO, start_when):
        """
        Control how and when to start crawling.

        (current) Distinguish INFO["TIME"] is `str` or `list`, then start crawling depends on the type.

        *Should only be called in run().*
        """

        # initialize logger
        log = Logger(file_name=self.__class__.__name__, debug_flag=True)
        log.session_start(self.__class__.__name__+' start', 0, '\n')

        # INFO checked
        self.INFO = INFO
        self.check_data()
        log.print_INFO(INFO)

        # wait until given start_when
        if start_when:
            log.session_start('wait until '+start_when, 0)
            TimeControl.start_when(start_when)
            log.session_end()

        # timer - start
        tic = time()

        # For single reservation time:        
        if isinstance(INFO["TIME"], str):
            log.session_start('run on single reservation time = '+INFO["TIME"],1, '\n')
            self.start(log=log)

        # For multiple reservation time:
        elif isinstance(INFO["TIME"], list):
            log.session_start('run on multiple reservation time' ,1, '\n')
            TIME_LIST = INFO["TIME"]
            for i in range(len(TIME_LIST)):
                INFO["TIME"] = TIME_LIST[i]
                log.session_start('time = '+INFO["TIME"] ,1, '\n')
                try:
                    self.start(log=log)
                    return
                except:
                    continue
        
        elapse = time() - tic
        print("elapse time: ", elapse, ' (sec.)')
        log.session_start("elapse time: " + "{:10.4f}".format(elapse) + ' (sec.)', 0, '\n')

    def dump_required_info(self):
        """
        Dump REQUIRED_INFO to file.
        """
        with open('REQUIRED_INFO.txt', mode='w', encoding='big5') as f:
            json.dump(self.REQUIRED_INFO,f,ensure_ascii=False)

    def read_info(self):
        """
        Read REQUIRED_INFO to self.INFO.        
        """
        with open('REQUIRED_INFO.txt', mode='r', encoding='big5') as f:
            self.INFO = json.load(f)    
    # -----------------------------------------------------------------------------#
    # costoumize method: MUST HAVE
    # -----------------------------------------------------------------------------#
    def check_data(self):
        """
         checking self.INFO    
        """
        

    def start(self, log:Logger):
        """
        start crawling process.

        ex: driver = DriverSetup()
            driver.get(self.url)
            ...

        """