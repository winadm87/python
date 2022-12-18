# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# import random
import random
import string
default_pass_len = '12'
default_pass_quantity = '12'
pass_len = input('How many symbols to generate (default is 12): \n') or default_pass_len
pass_quantity = input('How many passwords do you need (default 12): \n') or default_pass_quantity
chars = string.ascii_letters + string.digits + "!@#$%^&*.,?"
def genpass(pass_len):
    password = ''
    for i in range(int(pass_len)):
        password = password + random.choice(chars)
    print(f"Pass is: {password}")
for i in range(int(pass_quantity)):
    genpass(pass_len)