# ----------------------------------
# This script is used for learning
# The map() function takes a function and an iterable as arguments and
# calls the function with each item of the iterable.
# The function returns a map object and map objects are not
# subscriptable (cannot be accessed at an index).
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
print("lets calculate the some powers of number x.")
# define func to get power of number x
def cal_power(n):
    return x ** n
# ask user to define number x
x = int(input("Enter the value of x:\n"))
# define powers to calculate
powers = [2, 3, 4 , 5, 6, 7, 8, 9, 10]
# calculate. call map with func cal_power and define the list of powers
result = map(cal_power, powers)
# print the result. to be printed succesfully it must be showed as list
# print(list(result))
# or lets convert ot list first, and then print
result_list = list(result)
#print(result_list)
for res in result_list:
    print(res)
