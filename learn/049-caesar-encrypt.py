# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# Python ord() and chr() are built-in functions. They are used to convert a character to an int and vice versa. Python ord() and chr() functions are exactly opposite of each other
a = ord('a')
b = ord('b')
c = ord('c')
A = ord('A')
B = ord('B')
C = ord('C')
whitespace = ord(' ')
print(f"a is {a}, b is {b}, c is {c}, A is {A}, B is {B}, C is {C}, whitespace is {whitespace}")
for i in range(97, 123):
    print(i, chr(i))
for i in range(65, 91):
    print(i, chr(i))
#
#

def encrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            # take original char number + shift number - A-char place, taking modulo from 26 + A-char position
            result += chr((ord(char) + int(s) - 65) % 26 + 65)
        #Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + int(s) - 97) % 26 + 97)
    return result
# check the above function
text = input("Enter text to encrypt: \n")
s = input("Enter shift number: \n")

print(f"Plain Text is: {text}")
print(f"Shift pattern is: {str(s)}")
print(f"Cipher is: {encrypt(text, s)}")