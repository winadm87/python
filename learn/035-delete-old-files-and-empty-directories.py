#!/bin/python3
# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# set numbers of days to keep files, define folders to cleanup
# ----------------------------------
import os     # working with files and directories
import time   # work with time, get file creation date etc
# maximal age of files, older files will be deleted
days = 5
# list of folders to work with
folders = [
    "/home/admin7/musor",
    "/home/admin7/musor2"
]
# variables for stats
total_deleted_size = 0
total_deleted_files = 0
total_deleted_folders = 0

nowtime = time.time() # get current time in seconds
timeago = nowtime - 60*60*24*days # current time minus 5 days in seconds, if days set to 5

def delete_old_files(folder):
    """Delete files in directory older than x days"""
    # initialize global variables
    global total_deleted_files
    global total_deleted_size
    # path - full path to folder
    # dirs - just folder name
    # files - file name
    for path, dirs, files in os.walk(folder):
        for file in files:
            filename = os.path.join(path, file) # get full path to file
            filetime = os.path.getmtime(filename) # ctime - creation time, mtime - modification tim
            if filetime < timeago:
                sizefile = os.path.getsize(filename) # get file size
                total_deleted_size += sizefile # count total deleted space
                total_deleted_files += 1 # count number of deleted files
                print("deleting file", str(filename))
                os.remove(filename) # delete file

def delete_empty_dirs(folder):
    global total_deleted_folders
    emptydirs = 0 # count empty dirs for recursive run of function to remove all empty dirs on single run
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            total_deleted_folders += 1 # count empty folders
            emptydirs +=1
            print("Folder empty, removing:", str(path))
            os.rmdir(path) # delete folder
    if emptydirs > 0: # run recursively till all empty folders are deleted
        delete_empty_dirs(folder)
#-------------------main--------------
print("script started, folders for cleanup", folders)
start_time = time.asctime() # get current time in human readable format

for folder in folders:
    delete_old_files(folder)
    delete_empty_dirs(folder)

finish_time = time.asctime()
print("Start time", str(start_time))
print("Total deleted size:", str(int(total_deleted_size/1024/1024)), "MB")
print("Total deleted files:", str(total_deleted_files))
print("Total deleted empty folders", str(total_deleted_folders))
print("Finish time", str(finish_time))
