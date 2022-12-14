# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import sys
import os
# we will work with file originaltext.txt
# ask user for file and check if file available
original_file = input("Please insert full pah to original file: \n")
if(os.path.isfile(original_file)) == True:
    print("File found:", str(original_file))
    # original_text = open(original_file, mode='r', encoding='utf_8').read()
    with open(original_file, mode='r') as f:
        original_text = f.read()
else:
    # if original file not found - stop execution
    print("File not found:", str(original_file))
    print("Exiting, try another file")
    sys.exit()
# ask user to print file
ask_to_print = input("Print original file? - (yes/no) \n")
if ask_to_print == "yes":
    print("Original file content:", str(original_text))
# ask user what we want to change
what_to_change = input("Please insert text to be changed \n")
if what_to_change:
    print("This will be changed:", str(what_to_change))
    # lets look for inserted text in file
    with open(original_file, mode='r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(what_to_change) != -1:
                print(what_to_change, 'string exists in file')
                print('Line Number:', lines.index(line))
                print('Line:', line)
    # ask user to define what is desired text
    change_to_what = input("Please define to what change. If nothing defined - text will be deleted \n")
    print("You defined new string", str(change_to_what))
    # lets make the text change
    new_data = original_text.replace(str(what_to_change), str(change_to_what))
    # open original file with "write" mode
    with open (original_file, mode='w') as f:
        f.write(new_data)
    # ask user to print changed file
    ask_to_print = input("Print file after change? - (yes/no) \n")
    if ask_to_print == "yes":
        with open(original_file, mode='r') as f:
            new_file = f.read()
            print("Changed file now look like:", str(new_file))
else:
    print("Text to changed no defined, exiting...")
    sys.exit()
