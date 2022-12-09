names = ['masha','anzhela','Vasya','petya','volodya','Lena']
# print all list
print(names)
# print only first
print(names[0])
# print first from end
print(names[-1])
# count values in list
print(len(names))
# name to uppare case
print(names[0].upper())
# change item in list
names[2] = 'Alexander'
print(names)
# add an item to list
# append - to the end of ist
names.append('Kostya')
print(names)
# insert with index - place inside list
names.insert(1, 'Feofan')
print(names)
# remove from list
del names[-2]
print(names)
# or delete by value
names.remove('volodya')
print(names)
# and one more
deleted_name = names.pop()
print(deleted_name)
print(names)
# sort
names.sort()
print(names)
# reverse sort
names.sort(reverse=True)
print(names)
# just reverse the list
names.reverse()
print(names)