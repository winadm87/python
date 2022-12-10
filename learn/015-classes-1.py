# ----------------------------------
# This script is used for learning
# Classes are dictionaries with functions (methods) that affect this dictionaries
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
from hero import *

#-------------MAIN-------------------------------------
myhero1 = Hero("petka", 5, "orc")
myhero2 = Hero("verder", 3, "robot")

myhero1.show_hero()
myhero2.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(60)
myhero1.show_hero()
