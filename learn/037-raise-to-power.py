# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import math
print("lets solve math task to raise a number ot a power x in power n")
x = input("Please insert x: \n")
n = input("Please insert n: \n")
# Method 1
power = int(x) ** int(n)
print("(Calc by **) %d to the power %d is %d" % (int(x), int(n), power))
# Method 2
power = pow(int(x), int(n))
print("(Calc by pow) %d to the power %d is %d" % (int(x), int(n), power))
# Method 3
power = math.pow(2, 6.5)
print(f"(Calc by math.pow) Lets calculate 2 in power 6.5: {power}")