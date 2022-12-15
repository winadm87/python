# ----------------------------------
# This script is used for learning
# !Note - run this script from bash terminal for password to be hidden on definition
# Created by winadm
# Version 0.1
# Examples
# python3 040-getpass.py
# ----------------------------------
import getpass
passwd = getpass.getpass("Define password: \n")
# check password
if passwd == "123456":
    print("ok")
else:
    print("go away")