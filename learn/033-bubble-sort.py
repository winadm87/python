# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
list1 = [10, 44, 62, -4, 0, 1, 452, -13, 56, 8, 19]
def bubble_sort(list1):
    last_item = len(list1) - 1
    for x in range(0, last_item):
        for y in range(0, last_item-x):
            print(list1)
            if list1[y] > list1[y+1]:
                list1[y], list1[y+1] = list1[y+1], list1[y]

    return list1
print("original list", list1)
list2 = bubble_sort(list1).copy()
print("sorted list", list2)