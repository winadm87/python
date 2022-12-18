# ----------------------------------
# This script is used for ...
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import logging
# change the format of logging
logging.basicConfig(filename='example1.log', format='%(levelname)s:%(message)s', filemode='w', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')