# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
list1 = ['name', 'age', 'tel', 'email']
list2 = ['vasya', '20', '555-55-55', 'vasya@somedomain.com']
list3 = ['masha', '18', '666-66-66', 'masha@somedomain.com']
for v1, v2, v3 in zip(list1, list2, list3):
    print(v1, v2, v3)