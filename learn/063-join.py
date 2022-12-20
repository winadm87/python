# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# lets join tuple items using hash char as separator
tuple1 = ('vasya', 'petya', 'masha')
x = "#".join(tuple1)
y = ''.join(tuple1)
print(x)
print(y)
# lets define custom separator
dict1 = {
    'name': 'vasya',
    'country': 'cyprus',
    'email': 'someaddress@somedomain.com'
}
separator1 = 'HELLO'
x = separator1.join(dict1)
print(x)

s1 = 'abc'
s2 = '123'
# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# .join() with sets
test = {'2', '1', '3'}
s = ', '
print(s.join(test))
test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))