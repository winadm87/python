# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
list1 = (3, 5, 10, 15)
print(any([x > 10 for x in list1])) # true
print(any([x > 20 for x in list1])) # false

list2 = (1, 2, 3.3, 4, 5)
print(all(type(x) is int for x in list1)) # true
print(all(type(x) is int for x in list2)) # false
