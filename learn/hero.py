# ----------------------------------
# This script is used for learning classes
# Classes are dictionaries with functions (methods) that affect this dictionaries
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
class Hero():
    """Class to describe Heroes for our game"""
    def __init__(self, name, level, race):
        """initiate our Hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """print all parameters of this hero"""
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health)).title()
        print(description)
    def level_up(self):
        """upgrade hero level"""
        self.level += 1
    def move(self):
        """start moving hero"""
        print("Hero " + self.name + " start moving")
    def set_health(self, new_health):
        """set new health level"""
        self.health = new_health
