# ----------------------------------
# This script is used for ...
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
def convert_b_to_kb(total_b):
    bytes = total_b % 1024 # modulo
    kilobytes = total_b // 1024 # division without decimals

    print(f"{total_b} bytes = {kilobytes} kb and {bytes} b")
convert_b_to_kb(15300)

def convert_minutes_to_days(total_mins):
    days = total_mins // 1440
    extra_minutes = total_mins % 1440

    hours = extra_minutes // 60
    minutes = extra_minutes % 60

    print(f"{total_mins} = {days} days, {hours} hours, and {minutes} minutes")
convert_minutes_to_days(1507)