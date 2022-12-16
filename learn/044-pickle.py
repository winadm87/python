# ----------------------------------
# This script is used for learning
# pickle is used to serialize and deserialize some data
# it is converting data into byte stream
#
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import pickle
import random
# initialize empty list
dataobj = []
# put random numbers in list
# random.sample generate 5 randoms in range of 0-100
for i in random.sample(range(0, 100), 5):
    dataobj.append(i)
# lets look at list
print(dataobj)
# open file to be written to, 'wb' stands for binary format
file_handler = open('pickle_rick', mode='wb')
# write to file
pickle.dump(dataobj, file_handler)
# close file
file_handler.close()
# open file to read from it, 'rb' stands for binary format
file_handler = open('pickle_rick', mode='rb')
# read from file with pickle
dataobj = pickle.load(file_handler)
# print values
for value in dataobj:
    print(f"Current value is: {value}")
file_handler.close()
# try to print file with open... read()...
# this will fail, because file is encoded
file_handler = open('pickle_rick', mode='r')
text = file_handler.read()
print(text)
file_handler.close()

