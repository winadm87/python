# ----------------------------------
# This script is used for ...
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
string1 = "avada kedavra"
string_splitted = string1.split(' ')
print(string_splitted)
for i in string_splitted:
    i = i + "%s-ay" % (i[0]) #The %s token allows me to insert (and potentially format) a string. Notice that the %s token is replaced by whatever I pass to the string after the % symbol
    # "Hello %s, my name is %s" % ('john', 'mike')  # Hello john, my name is mike".
    # % s: string
    # % d: decimals
    # % f: float
    #print('%s %s\'s age is %d with incredible IQ of %f ' % (name, extendedName, age, IQ))  # Gandalf the Grey's age is 84 with incredible IQ of 149.900000
    print(i)
    i = i[1:] # split one letter from left
    print(i)
# once more example string % values
print("%s %s" % ("a", "b"))
print("%s" % "some text")
# join
message = ' '.join(['this' ,'is', 'a', 'useful', 'method'])
print(message)
message = "this is an example".split(" is ")
print(message)
message = "this is an example".partition(" is ")
print(message)
# f-string example
# The end parameter for print() is an empty string ("") so it won’t output a newline at the end of the string
# -^15 output 15 chars, center align, fill any space with (-)
name = "vasya"
print(f'{name:-^15}', end='')
print('\n')
print('this {0} string'.format('is'))
print('this {word} string'.format(word='is'))