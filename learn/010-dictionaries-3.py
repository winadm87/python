# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# define new dictionary
customers = {
    '010101' : 'nick cave',
    '020202' : 'john travolta',
    '030303' : 'gio pika',
    '040404' : 'kravc',
}
# append a new data to list
customers['050505'] = 'endshpil'
# print customers:
for customer in customers:
    print(customers[customer])
# ask user to define id to search
id = input("Enter id to search: \n")
# search the id in the dictionary
for customer in customers:
    if customer == id:
        print(customers[customer])
        break