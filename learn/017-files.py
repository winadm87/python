# ----------------------------------
# This script is used for learning work with files
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
inputfile1 = "usernames.txt"
# open() - pointer to file, mode r(read) etc
myfile1 = open(inputfile1, mode='r', encoding='utf_8')
# print all
#print(myfile1.read())

# print string by string
for num, line in enumerate(myfile1):
    print(str(num + 1) + " Hello " + line.strip())

# print only if statement true
for num, line in enumerate(myfile1):
    if "Key" in line:
        print(str(num + 1) + " Hello " + line.strip())

inputfile2 = "passwords.txt"
outputfile2 = "selectedpasswords.txt"
passwordtolookfor = "a"
# open() - pointer to file, mode r(read), w(write), a(append) etc
myfile2 = open(inputfile2, mode='r', encoding='utf_8')
myfile3 = open(outputfile2, mode='a', encoding='utf_8')
# print all
#print(myfile2.read())
for num, line in enumerate(myfile2):
    if passwordtolookfor in line:
        print(str(num + 1) + " Password is  " + line.strip())
        # overwrite to file
        myfile3.write('found password with "a" letter: ' + line)

myfile1.close()
myfile2.close()
myfile3.close()