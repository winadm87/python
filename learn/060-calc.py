# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import logging
import sys
logging.basicConfig(filename='calc.log', format='%(asctime)s %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S %d.%m.%Y', filemode='w', level=logging.DEBUG)
def inputnumbers():
    try:
        logging.info('Asking user for numbers')
        global n1, n2
        n1 = float(input('Input number n1: \n'))
        n2 = float(input('Input number n2: \n'))
        logging.info(f'User defined numbers {n1} and {n2}')
        print(f'numbers {n1} and {n2} are set to be used further')
    except Exception as e:
        print(f'Got an exception: {e}, try again to insert correct numbers')
        logging.error(f'Numbers input failed with: {e}')
        inputnumbers()

def addiction(inputnumbers):
    try:
        logging.info(f'Trying to perform addiction operation on numbers {n1} and {n2}')
        summ1 = n1 + n2
        print(f'Summ of numbers {n1} and {n2} is: {summ1}')
        logging.info(f'Summ is equal to: {summ1}')
    except Exception as e:
        print(f'Got an exception: {e}')
        logging.error(f'Addiction operation failed with error: {e}')

def subtraction(inputnumbers):
    try:
        logging.info(f'Trying to perform subtraction operation on numbers {n1} and {n2}')
        subt1 = n1 - n2
        print(f'Subtraction of numbers {n1} and {n2} is: {subt1}')
        logging.info(f'Subtraction is equal to: {subt1}')
    except Exception as e:
        print(f'Got an exception: {e}')
        logging.error(f'Subtraction operation failed with error: {e}')

def multiplication(inputnumbers):
    try:
        logging.info(f'Trying to perform multiplication operation on numbers {n1} and {n2}')
        mult1 = n1 * n2
        print(f'Multiplication of numbers {n1} and {n2} is: {mult1}')
        logging.info(f'Multiplication is equal to: {mult1}')
    except Exception as e:
        print(f'Got an exception: {e}')
        logging.error(f'Multiplication operation failed with error: {e}')

def division(inputnumbers):
    try:
        logging.info(f'Trying to perform division operation on numbers {n1} and {n2}')
        div1 = n1 / n2
        print(f'Division of number {n1} by {n2} is: {div1}')
        logging.info(f'Division is equal to: {div1}')
    except Exception as e:
        print(f'Got an exception: {e}')
        logging.error(f'Division operation failed with error: {e}')

def choose_operation():
    print('Please choose operation to perform')
    choose = input('Insert "a" for addiction, "s" - subtraction, "m" - multiplication, "d" - division: \n')
    if choose == 'a' or choose == 'add' or choose == 'addiction':
        logging.info('User chosen addiction')
        addiction(inputnumbers())
        try_again_operation()
    elif choose == 's' or choose == 'sub' or choose == 'subtraction':
        logging.info('User chosen subtraction')
        subtraction(inputnumbers())
        try_again_operation()
    elif choose == 'm' or choose == 'mul' or choose == 'multiplication':
        logging.info('User chosen multiplication')
        multiplication(inputnumbers())
        try_again_operation()
    elif choose == 'd' or choose == 'div' or choose == 'division':
        logging.info('User chosen division')
        division(inputnumbers())
        try_again_operation()
    else:
        logging.warning(f'User have chosen strange operation {choose}, re-asking for input')
        print(f'Operation {choose} is not defined, try again')
        choose_operation()

def try_again_operation():
    logging.info('Operation completed, asking for continue')
    try_again = input('Operation completed, try another operation (y/n)? \n')
    if try_again == 'y' or try_again == 'yes' or try_again == 'Yes' or try_again == 'YES':
        choose_operation()
    else:
        print('Execution stopped, exiting...')
        logging.info('Script execution completed, exiting')
        sys.exit()

#------------------main-------------------

logging.info('Execution of the calc script is started')
logging.info('Asking user for operation type')
choose_operation()
