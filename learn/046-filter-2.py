# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# define empty list
numbers = []
# put some in the list
for i in range(0, 20):
    numbers.append(i)
#print(numbers)
# define func to find even numbers
def find_even(number):
    if number % 2 == 0:
        return True
    return False
# define func to find odd numbers
def find_odd(number):
    if number % 2 == 1:
        return True
# run filters
even_numbers = filter(find_even, numbers)
odd_numbers = filter(find_odd, numbers)
# and print results
print(list(even_numbers))
print(list(odd_numbers))
