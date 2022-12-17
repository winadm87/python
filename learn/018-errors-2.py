# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
list1 = ['a', 'b', 'c', 'd']
index1 = int(input("Enter values of index to be searched in list:"))
try:
    print(list1[index1])
except IndexError as e:
    print(f"Got an exception: {e}")
else:
    print("this string appears only if no exception occure")
finally:
    print("this string appears anyway, even if exception occure")