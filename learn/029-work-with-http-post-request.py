# ----------------------------------
# This script is used for learning
# HTTP POST
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# import modules
from urllib import request, parse
import sys
# define url to send POST request
url1 = "https://google.com/search?"
# in vaue we define what exactly we a looking for
value1 = {'q': 'python lessons'}
# we need to define some headers for google. if not - google will throw 403 Forbidden, as we are robots)
headers1 = {}
headers1['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
# try request
try:
    # parse correct format from value1 variable
    value1_enc = parse.urlencode(value1)
    #print(value1_enc)
    # combine url with our request
    url1 = url1 + value1_enc
    #print(url1)
    # make a request, add headers
    req1 = request.Request(url1, headers=headers1)
    response1 = request.urlopen(req1)
    # read response line by line
    response1 = response1.readlines()
    for line in response1:
        print(line)
except Exception:
    print("Error occured")
    print(sys.exc_info()[1])