# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import sys
filename = "thisisfile.txt"
try:
    print("inside try")
    myfile = open(filename, mode='r', encoding='utf_8')
except Exception:
    print("inside except")
    print("error found")
    print("Error is :" + str(sys.exc_info()[1]))
    #sys.exit() # break execution of the script
    #filename = input("Input correct filename")
else:
    print("inside else")
    print(myfile.read())
finally:
    print("inside finally")

print("123")