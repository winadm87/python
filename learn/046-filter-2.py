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
for i in range(1, 20):
    numbers.append(i)
#print(numbers)
# define func to find even numbers
def find_even(number):
    if number % 2 == 0:
        return True
    return False
# define func to find odd numbers
def find_odd(number):
    if number % 2 != 0:
        return True
# run filters
even_numbers = filter(find_even, numbers)
odd_numbers = filter(find_odd, numbers)
# and print results
print(list(even_numbers))
print(list(odd_numbers))
print("===============")
# lets try lambda func to the same operation
numbers_new = []
# put some in the list
for i in range(1, 20):
    numbers_new.append(i)
# lambda (arguments): expression
even_numbers_new = list(filter(lambda x: (x%2 == 0), numbers_new))
print(even_numbers_new)
print("===============")
# use filter with None. it will filter out all boolean False's
my_list = [5, -23, "", True, False, 0, 0.0, {}, []]
filtered_object = filter(None, my_list)
for element in filtered_object:
   print(element)
print("===============")
# letrs try iler on a list of dictionaries
books = [
   {"Title":"Angels and Demons", "Author":"Dan Brown", "Price":500},
   {"Title":"Gone Girl", "Author":"Gillian Flynn", "Price":730},
   {"Title":"The Silent Patient", "Author":"Alex Michaelidis", "Price":945},
   {"Title":"Before I Go To Sleep", "Author":"S.J Watson", "Price":400}
   ]
def func(book):
   if book["Price"] > 500:
       return True
   else:
       return False
filtered_object = filter(func, books)
for d in filtered_object:
   print("Books with price over 500: ", dict(d)["Title"])