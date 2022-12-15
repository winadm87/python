# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
hello_string = "Hello world!"
print(f"This is basic string {hello_string}")
print("And this is basic string {hello_string}")
# the "f" allows us to insert variable into output. without it we have to print var after quotes, like this
print("And once again:", hello_string)
# also we can use conver to str or repr
print("String with str:", str(hello_string))
print("String with repr:", repr(hello_string))
# as you can see we have quotes in output using repr()