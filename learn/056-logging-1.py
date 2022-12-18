# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import logging
# remove filemode='w' to append data to log file
logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
print("Logging?")
# logging variables
logging.warning('%s before you %s', 'Look', 'leap!')
var1 = "abc"
var2 = "MF"
logging.warning(f'this is var1 - {var1} and var2 - {var2}')
