# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
some_text = "this is long string to practice slising in pyhton"
print(f"Original text is: {some_text}")
# slice takes 3 parameters, (start, stop, step)
# if only 1 condition is mentioned - it will be "stop"
slice_text = slice(8)
print(f"Sliced with only stop, number 8 is defined: {some_text[slice_text]}")
# if two operands are defined - first is start, second is stop
slice_text = slice(8, 15)
print(f"Sliced with two operands 8 and 15: {some_text[slice_text]}")
# if all three operands are defined, there will be start, stop and step
slice_text = slice(8, 25, 5)
print(f"All three operands are set to 8, 25 and 5 as step. The result is: {some_text[slice_text]}")