# ----------------------------------
# This script is used for learning working with json
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import json

filename = "user_settings.txt"
file1 = open(filename, mode='w', encoding='utf_8')
user1 = {
    'username': "Donald Duck",
    'score': 17,
    'awards': ["medal of honor", "snoring master", "sleeper numba 1"]
}
user2 = {
    'username': "scroodge8",
    'score': 8,
    'awards': ["top of the bottom", "bot winner"]
}
# create empty array
users = []
# add users to array
users.append(user1)
users.append(user2)
# print(users)
# ----------save to json-------------
# dump json to file
json.dump(users, file1)
# close file
file1.close()
#-----------load from json-----------
file1 = open(filename, mode='r', encoding='utf_8')
json_file1 = json.load(file1)
print(json_file1)
for user in json_file1:
    print("username is: " + str(user['username']))
    print("score is: " + str(user['score']))
    print("award numba 1 is: " + str(user['awards'][0]))
    print("awards are: " + str(user['awards']))
    print("-----------------------------------")