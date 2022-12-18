# ----------------------------------
# This script is used for ...
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import logging
# or make some custom date\time format with
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.basicConfig(filename='example2.log', format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)
logging.warning('is when this event was logged.')