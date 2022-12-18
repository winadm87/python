# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
user_input = int(input("Enter the number to reverse: \n"))
_rev = 0
while(user_input > 0):
    print(f"user_input now is {user_input}")
    # go for the last digit in original number by modulo with 10
    dig = user_input % 10 # working with the last number
    print(f"dig is {dig}")
    # setting reverse number by multiplying on 10 and adding dig from the previous step
    _rev = _rev * 10 + dig
    print(f"_rev is {_rev}")
    # throwing away the last number bu deleting without decimals (//)
    user_input = user_input//10
print(f"The reversed number is: {_rev}")