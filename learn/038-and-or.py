# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import re
print("Lets try some and\or statements")
nickname = input("Please define your nickname: \n")
if len(nickname) <= 3:
    print(f"Nickname {nickname} is too short, min 4 symbols")
else:
    print(f"{nickname} ok")
password = input("Please define your password: \n")
if (len(password) < 6) or (str(nickname) == str(password)):
    print("Password must be more than 6 symbols and must NOT be equal to nickname!")
else:
    print("Password is ok")
email = input("please enter an email address to get spam: \n")
if (len(email) > 0) and (re.search('@', email)) and (re.search('^(?!@)', email)):
    print(f"Email address set to: {email}")
else:
    print(f"email address {email} invalid (doesnt contain @ or starts with it)")