# ----------------------------------
# This script is used for learning regexp
# Try to use https://regex101.com/ for help in generating valid expression
# 1. Choose python on the left
# 2. insert piece of code
# 3. try some combinations
# 4. on the bottom right you can find some tips
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import re
# define file in the same folder, or use full path, f.e. /opt/garbage/usernames.txt
filename = "usernames2.txt"
# define file to write results to
resultfile = "results.txt"
# open both files, first to read from, second to append results
mytext = open(filename, mode='r', encoding='utf_8').read()
myresult = open(resultfile, mode='a', encoding='utf_8')
#print(mytext)
print("Looking for emails in garbage")
# any word charachters, minuses (-) or dots (.). All other symbols (including +)
# cant be used in email address. Then we define @.
# Then we exclude intel.com (?!intel\.com) from results and
# add some other words with dots and minuses [\w.-]+.
lookfor = r"[\w.-]+\@(?!intel\.com)[\w.-]+"
result = re.findall(lookfor, mytext)
for i in result:
    print("Found email: " + str(i))
    myresult.write(str(i) + "\n")
print("Looking for tel in garbage")
# we can start with + or not - [\+]?. We can have some country prefix [78]?. Next we
# have 10 numbers. This is pattern for mobile numbers.
lookfor = r"[\+]?[78]?[\d]{10}"
result = re.findall(lookfor, mytext)
for i in result:
    print("Found tel: " + str(i))
    myresult.write(str(i) + "\n")
