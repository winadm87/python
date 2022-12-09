enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': "green",
    'health': 100,
    'name': 'suhar',
    'ammo': ['pistol','knife']
}
# create array
all_enemies = []
# add enemies in array
for x in range(0,10):
    all_enemies.append(enemy.copy()) # add copy of enemy
for i in all_enemies:
    print(i)
print(all_enemies)
# lets change some parameter
all_enemies[2]['health'] = 30
all_enemies[0]['name'] = "golub"
print(all_enemies)