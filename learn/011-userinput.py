# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
name = input("Please enter a name: ")
print("Privet " + name)
# ask user for two numbers and sum them
n1 = input("Enter number x: ")
n2 = input("Enter number y: ")
sum = int(n1) + int(n2)
print(sum)
# asl user for password, check it truth
message = ""
while True :
    message = input("Enter password: ")
    if message == 'secret':
        break
    print(message + " password not correct")

list1 = []
msg = ""
while msg != 'stop':
    msg = input('Enter new item to add to list (enter "stop" to finish): ')
    list1.append(msg)
print(list1)