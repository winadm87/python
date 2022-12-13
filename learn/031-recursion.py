# ----------------------------------
# This script is used for learning
# Recursive function is calling itself
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# lets define basic recursive function
# this func will run eternally, or interpreter will kill the process with error
#def privet():
#    print("Hello world")
#    privet()
#privet()

# now lets write recursive function with specific iteration value
def hello(x):
    # stop execution when x = 0. This is called "the base condition."
    if x == 0:
        return
    else:
        # print as much as x-1 while x wont be equal to 0, than stop execution
        print("Hello world")
        hello(x-1)
hello(2)

# lets write func for sum 0+1+2+3+4+5 etc
def summ1(x):
    # This is called "the base condition."
    if x == 0:
        return 0
    #elif x == 1:
    #    return 1
    else:
        return x + summ1(x-1)

z = summ1(5)
print(z)

# lets write func to factorial 5! = 1*2*3*4*5
def fact1(x):
    # This is called "the base condition."
    if x == 0:
        return 1
    else:
        return x * fact1(x-1)
print(fact1(5))

# lets write function for fibonacci 0,1,1,2,3,5,8,13,21,34,55
def fibb1(x):
    # This is called "the base condition."
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibb1(x - 1) + fibb1(x - 2)
print(fibb1(7))