# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import os
# set path to look files in
path = '/home/admin7/gitroot/python/learn'
# read contents of dir
files = os.listdir(path)
# print contents
for file in files:
    print(file)
