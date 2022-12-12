# ----------------------------------
# This script is used for learning
# HTTP download file
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
from urllib import request
import sys

url1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSL5Kd15eKxhhEXIIrRuTPwG_4Q9Vf3X432Pg&usqp=CAU"
file1 = "/tmp/picture1.jpg"

try:
    print("Start downloading file from " + url1)
    request.urlretrieve(url1, file1)
    print("File downloaded to " + file1)
except Exception:
    print("error occured")
    print(sys.exc_info()[1])

