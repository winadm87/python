# ----------------------------------
# This script is used for learning arguments
# Created by winadm
# Version 0.1
# Examples
# from cli run
# python3 020-cli-arguments.py
# python3 020-cli-arguments.py aaa bbb ccc
# ----------------------------------
# to use argv import sys
import sys
# run OS commands
import os
print("hello")
# print arguments from cli, slice name of script - 020-cli-arguments.py
print(sys.argv[1:])
x = len(sys.argv)
if x > 1:
    print("cli argumnts are: " + str(sys.argv[1:]))
else:
    print("arguments no defined")
y = len(sys.argv)
if y > 1:
    if sys.argv[1] == "/?":
        print('Help requested, look "man python3" or just google it))')
# run OS command
os.system("ls -al | grep cli")
# exit from script with custom error leve
sys.exit(2)