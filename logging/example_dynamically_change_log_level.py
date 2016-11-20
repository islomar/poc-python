import logging
import signal    
import os   
from time import sleep 

class MyLogging(object):
    
    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)
    
    def getLogger(self):
        return self.logger

    # kill -USR1 <pid>
    def changeLogLevelToDebug(self, signal_number, interrupted_stack_frame):
        print 'Signal handler called with signal', signal_number
        print(os.environ.get('LOG_LEVEL'))
        logger.setLevel(logging.DEBUG)

    # kill -USR2 <pid>
    def changeLogLevelToInfo(self, signal_number, interrupted_stack_frame):
        print 'Signal handler called with signal', signal_number
        print(os.environ.get('LOG_LEVEL'))
        logger.setLevel(logging.INFO)


if __name__ == '__main__':

    # create logger
    my_logging = MyLogging('simple_example')
    logger = MyLogging('simple_example').getLogger()
    logger.setLevel(logging.INFO)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

    #We configure the signal handlers
    signal.signal(signal.SIGUSR1, my_logging.changeLogLevelToDebug);
    signal.signal(signal.SIGUSR2, my_logging.changeLogLevelToInfo);

    while True:
        sleep(1)
        logger.info('Probando... pid: %s', os.getpid())
        logger.debug('Probando... pid: %s', os.getpid())