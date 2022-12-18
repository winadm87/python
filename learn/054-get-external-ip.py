# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import requests
# define url to send request to
ur_url = "http://checkip.dyndns.org"
# send a request
request = requests.get(ur_url)
full_result = request.text
print(full_result)
# split the response result by two dots in it and take the second part of the split
_result = request.text.split(': ', 1)[1]
print(_result)
# split again and take only ip
your_ip = _result.split('</body></html>', 1)[0]

print(your_ip)