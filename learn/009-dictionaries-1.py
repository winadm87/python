enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': "green",
    'health': 100,
    'name': 'suhar',
}
print(enemy)
print("location x: " + str(enemy['loc_x']))
print("location y: " + str(enemy['loc_y']))
print("name is " + enemy['name'])
# add parameters tp object
enemy['rank'] = 'soldier'
print(enemy)
# remove parameter from object
#del enemy['health']
#print(enemy)
# change parameters
enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 40
if enemy['health'] < 75:
    enemy['color'] = 'yellow'
print(enemy)

print(enemy.keys())
print(enemy.values())

