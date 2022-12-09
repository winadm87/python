langs = ['go', 'Python', 'pascal', 'Assembler', 'RoR', 'java', 'JS', 'kotlin']
print(langs)
# print by loop
for i in langs:
    print(i)
    print(i.upper())
for x in range(1,10):
    print(x)
mynumber_list = list(range(0,10))
print(mynumber_list)
# work with list in loop
for m in mynumber_list:
    m = m * 3
    print(m)
# find min\max value in list
print("max number is: "+ str(max(mynumber_list)))
print("min number is: "+ str(min(mynumber_list)))
# find sum
print("sum of list is: "+ str(sum(mynumber_list)))
# create list from another list
mylangs = langs[1:4]
print(mylangs)
# from first
mylangs2 = langs[:4]
print(mylangs2)
# from end
mylangs3 = langs[-3:-1]
print(mylangs3)
# make copy of list
mylangs4 = langs[:]
print(mylangs4)