#!/bin/python3
# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# python3 034-log-purge.py log1.txt 10              5
#         ^script          ^log     ^size treshold  ^ how many logs to store
# ----------------------------------
import shutil  # for copyfile
import os      # for getfilesize and check if file exists
import sys     # for cli arguments

# check for cli arguments, need all 4 to run our script
if(len(sys.argv) < 4):
    print("Missing arguments, usage is script.py log.name size.kb amount.archives")
    exit(1)
# create 3 inputs for our script
# logname - main log name that should be shrinked
logname = sys.argv[1]
# ask user to set filesize treshold, if treshold is reached - script will copy main file to _1 and flush main file
treshold = int(sys.argv[2])
# ask user to define amount of _* files to store
archive_amount = int(sys.argv[3])
# check if main logfile exists
if(os.path.isfile(logname)) == True:
    # get main logfile size in bytes
    logfile_size = os.stat(logname).st_size
    # convert from B to KB
    logfile_size = logfile_size / 1024
    # check if main logsize file above defined treshold
    if(logfile_size >= treshold):
        # check if user set amount of stored file more than zero
        if(archive_amount > 0):
            # for every _* file run rename operation
            for currentfilenumber in range(archive_amount, 1, -1):
                # set filenames
                src = logname + "_" + str(currentfilenumber - 1)
                dst = logname + "_" + str(currentfilenumber)
                # check that old file exist
                if(os.path.isfile(src) == True):
                    # copy old file with new name
                    shutil.copyfile(src,dst)
                    print("copied:", src, "to", dst)
            # copy main file with _1
            shutil.copyfile(logname, logname + "_1")
            print("copied:", logname, "to", logname + "_1")
        # flush main file with open and "w"rite
        myfile = open(logname, "w")
        myfile.close()


