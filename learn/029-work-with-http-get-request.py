# ----------------------------------
# This script is used for learning
# HTTP GET
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
from urllib import request

url1 = "https://github.com"
response = request.urlopen(url1)
text1 = response.readlines()
text2 = response.read()
# print response
#print(response)
# print response readed line by lien
#for string in text1:
#    print(string)
# just print readed response
print(text2)