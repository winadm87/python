# ----------------------------------
# This script is used for learning regexp basics
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# \d - any digit 0-9
# \D - any not digit
# \w - any alphabet symbol [A-Z a-z]
# \W - any NOT alphabet symbol
# \s - breakspace
# \S - not breakspace

# {3} - 3 of something
# [a-z]+ - any number of small letters
# any special symbols shoud go with slash, for example \. or \"
# first import re to work with regexp
import re
file1 = "usernames2.txt"
# read text file to variable
mytext = open(file1, mode='r', encoding='utf_8').read()
# print(mytext)
# simple
texttolookfor = r"Dav"
allresults = re.findall(texttolookfor, mytext)
print(allresults)
# find 4 numbers in a row
texttolookfor1 = r"\d{4}"
allresults1 = re.findall(texttolookfor1, mytext)
print(allresults1)
# find 6 non numbers with a space after them
texttolookfor2 = r"\w{6}\s"
allresults2 = re.findall(texttolookfor2, mytext)
print(allresults2)
# find names - first capital letter and then any number of small letters
texttolookfor3 = r"[A-Z][a-z]+"
allresults3 = re.findall(texttolookfor3, mytext)
print(allresults3)
# search for domains
texttolookfor4 = r"\w+\.\w+"
allresults4 = re.findall(texttolookfor4, mytext)
print(allresults4)
# search for email addresses
texttolookfor5 = r"\w+\@\w+\.\w+"
allresults5 = re.findall(texttolookfor5, mytext)
print(allresults5)