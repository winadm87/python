# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
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
