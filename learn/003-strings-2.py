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