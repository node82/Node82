import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)  # turn off logging except for critical errors             
             
logging.debug('start of program')
logging.debug('start of function')
logging.error('this should cause an error')
logging.warning('warning of function')
logging.debug('end of program')
                  
#log levels
#    debug (lowest)
#    info
#    warning
#    erorr
#    critical(highest)
