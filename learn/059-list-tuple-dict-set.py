# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# string - a list, cannot be changed with text[0] = 'a'
# list [] - can be changed
# tuple () - can not be changed
# set {} - is an unordered collection (NO INDEX) data type that is iterable, mutable, and has no duplicate elements. Python’s set class represents the mathematical notion of a set.
# dict {} - key-value pair

# Lists
l = []
# Adding Element into list
l.append(5)
l.append(10)
print(f"Adding 5 and 10 in list {l}")
# Popping Elements from list
l.pop()
print(f"Popped one element from list {l}")
print()

# Set
s = set()
# Adding element into set
s.add(5)
s.add(10)
print(f"Adding 5 and 10 in set {s}")
# Removing element from set
s.remove(5)
print(f"Removing 5 from set {s}")
print()

# Tuple
t = tuple(l)
# Tuples are immutable
print(f"Tuple {t}")
print()

# Dictionary
d = {}
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print(f"Dictionary {d}")
# Removing key-value pair
del d[10]
print(f"Dictionary {d}")