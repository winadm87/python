# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import datetime
from datetime import *

# read current date
current_date = date.today()
print(f"Today is {current_date}")
# another variant
# rint the formatted date
print("Today is: %d-%d-%d" % (current_date.day, current_date.month, current_date.year))
print(f"Today is {current_date.day}-{current_date.month}-{current_date.year}")

# Set the custom date
custom_date = date(2020, 12, 16)
print(f"The custom date is: {custom_date.day}-{custom_date.month}-{custom_date.year}")

# calculated date, lets try to divide pare of dates
calculated_date = custom_date - current_date
print(f"Calculated date is: {calculated_date}")

# lets play with full date and time
current_date_time = datetime.now()
print(f"Current date and time is {current_date_time}")
print(f"Current formatted date and time is {current_date_time.hour}-{current_date_time.minute}--{current_date_time.day}-{current_date_time.month}-{current_date_time.year}")
date_time_formatted = str(current_date_time.hour) + "-" + str(current_date_time.minute) + "--" + str(current_date_time.day) + "-" + str(current_date_time.month) + "-" + str(current_date_time.year)
print(date_time_formatted)
filename = "testlog_" + date_time_formatted + ".log"
print(filename)
logfile = open(filename, mode='w')
logfile.write("This is test file")