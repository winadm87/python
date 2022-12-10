# ----------------------------------
# This script is used for ...
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

class SuperHero(Hero):
    """Class to create superhero"""
    def __init__(self, name, level, race, magiclevel):
        """initiate our superher"""
        super().__init__(name, level, race)
        #self.magiclevel = magiclevel
        self.magic = 100
    def makemagic(self):
        """use magic"""
        self.magic -= 10
    def show_hero(self):
        """print all parameters of this hero"""
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health) + " Magic is: " + str(self.magic)).title()
        print(description)