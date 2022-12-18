# ----------------------------------
# This script is used for ...
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import logging
logging.basicConfig(filename='example4.log', format='%(asctime)s %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S %d.%m.%Y', filemode='w', level=logging.DEBUG)
logging.info('Execution of the script is started')
logging.info('Lets try-catch exception and write it to log as error-level')
list1 = ['a', 'b', 'c']
idx = input('please define the index: \n')
try:
    print(list1[int(idx)])
    logging.info(f'value with index {idx} is {list1[int(idx)]}')
except IndexError as e:
    print(f"Got an exception: {e}")
    logging.error(f'While searching list for index error occured: {e}')