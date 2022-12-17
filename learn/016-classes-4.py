# ----------------------------------
# This script is used for ...
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
class Dog:

    def __init__(self, name):
        self._name = name  # underscore (_) is used to define "private" attributes

    @property
    def name(self):
        print("Calling getter")
        return self._name

    @name.setter
    def name(self, new_name):
        print("Calling setter")
        self._name = new_name

    @name.deleter
    def name(self):
        print("Calling deleter")
        del self._name

#------------------main---------------

dog1 = Dog("sharik")
print(dog1.name) # calling getter
dog1.name = "korzhik" #calling setter
print(dog1.name) # calling setter
del dog1.name # calling deleter
print(dog1.name)