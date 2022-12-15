# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# import another script
import emails as v
# call for list in another script and print it
print(f"Emails to look for are {v.emails}")
# define file to check strings in it
original_file = "originaltext.txt"
# open file in read mode
with open(original_file, mode='r') as f:
    # read file line by line
    lines = f.readlines()
    # for each line ...
    for line in lines:
        # for each defined email in another script
        for email in v.emails:
            # check if current line contains email
            if line.find(email) != -1:
                # print email and line where it was found
                print(f"Email {email} string exists in file {original_file} on line {lines.index(line)}")
