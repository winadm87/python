# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# define two variables and print them
a = "Hello"
b = "John"
age = 25
print(a + ' ' + b)
# or combine variables into third one and print it instaed
combined = a + " " + b
print(combined)
# and lets convert age to string
print(combined + " " + str(age))
# lets work with register
s_name = "ivanov"
S_name = "IVANOV"
print(s_name + " ---- " + S_name)
# and a little work with numbers
n1 = 111
n2 = 555
sum = n1 + n2
print(n1+n2)
print(str(n1) + "+" + str(n2) + "=" + str(sum))
# lets look at f-string
value = 5
print(f"The base value is {value}, it must be multiplied by 10, so the new value is: {value*10}")
# swap values
a = 1
b = 2
print(f"a = {a}, b = {b}")
a, b = b, a
print(f"a = {a}, b = {b}")