# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
def privet():
    """print privet"""
    print("Eto function test - Privet!")

def zdarova(name):
    """print zdarova with input name"""
    print("Zdarova " + name)
privet()
zdarova("vasya")
def summochka(x, y):
    print(x+y)
summochka(10, 20)

def summochka1(x, y):
    return x + y
m = summochka1(5, 22)
print(m)

def factorial(i):
    """calculate factorial"""
    fact = 1
    for i in range(1, i+1):
        fact = fact * i
    return fact
print(factorial(3))
for i in range(1, 10):
    print("factorial from " +  str(i) + " is equal:" + str(factorial(i)))



