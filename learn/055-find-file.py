# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import os
import fnmatch
path = "/home/admin7/gitroot/python/learn"
pattern = "emails.py"
#pattern = "*.py"
#list1 = os.walk(path)
#print(list(enumerate(list1)))
#print(list(list1))
for root, dirs, files in os.walk(path):
    for file in fnmatch.filter(files, pattern):
        print(os.path.join(root, file))