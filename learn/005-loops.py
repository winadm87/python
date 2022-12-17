# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# for loop
# this loop will show first empty string, because str*0 = 0
for i in range(5):
    print("Hello-" * i)
print("first loop")
for x in range(0, 10):
    print("current x:" + str(x + 1))
print("second loop")
for i in range(0, 10, 2):
    print("current i:" + str(i))
print("third loop")
for n in range(0, 10):
    print(n)
    if n == 5:
        print("ouch")
        break
print("once more loop")
for m in range(10, 0, -2):
    print(m)
# infinite loop
y = 0
while True:
    print(y)
    y = y + 1
    if y == 50:
        break
