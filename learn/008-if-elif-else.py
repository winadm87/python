x = 14
if x == 15:
    print('YES you are right')
else:
    print('You are wrong')

age = 12
if age <= 4:
    print('you are to young')
elif age > 4 and age <= 18:
    print('you have to grow up')
else:
    print('earn some money and die')

names = ['masha','anzhela', 'David', 'Vasya', 'petya', 'volodya', 'Lena', 'John']
norus_names = ['David', 'John']

if 'anzhela' in names:
    print('anzhela found in list')
else:
    print('anzhela not found in the list')

for name in names:
    if name in norus_names:
        print(name + ' no rus name')
    else:
        print(name + ' rus name')