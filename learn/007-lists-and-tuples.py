# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# define list
list1 = ["a", "b"]
print(list1)
type1 = type(list1)
print(type1)
print("============")
# define tuple
tuple1 = ("a", "b")
print(tuple1)
type2 = type(tuple1)
print(type2)
print("============")
# use list values as variables, its called packing\unpacking
list2 = ["a", "b", "c"]
var1,var2,var3 = list2
print(var1, var2, var3)
print("============")
# lets try to change tuple value
#names = ("vaysa", "masha", "albina")
#names[0] = "andrey"
# TypeError: 'tuple' object does not support item assignment
print("============")