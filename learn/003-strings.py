# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
mystring = "hello pychar"
name = "mr petr puSHkin"
print(name)
print(name[0])
# lets up first letters
print(name.title())
# lets up all leterrs
print(name.upper())
# lets low all letters
print(name.lower())
# lets go to another string
print("Privet\nPoka")
# lest use tab
print("messages:\n\tmessage1\n\t\tmessage2")
# lets work with cut, rstrip - from right, lstrip - from left, strip - from both sides
a = " . . ogon gorit . "
print(a)
print(a.rstrip())
print(a.lstrip())
print(a.strip())
print(a.strip(" "))
b = a.strip()
print(b.strip("."))