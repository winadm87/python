# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# lets define array
list1 = [10, 12, 14, 15, 16, 18, 21, 23, 27, 30, 31, 33, 35, 39, 44, 49, 51, 55, 56, 57, 67, 77, 80, 83]
# lets define func for searching, it will take our array, num1 - number to find, start - from which index to start, stop - to which index looking
def binarysearch(list1, num1, start, stop):
    if start > stop:
        return False
    else:
        # search for middle, "//" used to get round number, without decimal values
        mid = (start + stop) // 2
        if num1 == list1[mid]:
            return mid
        elif num1 < list1[mid]:
            return binarysearch(list1, num1, start, mid - 1)
        else:
            return binarysearch(list1, num1, mid + 1, stop)


num1 = 19
x = binarysearch(list1, num1, 0, len(list1))
if x == False:
    print("Item " + str(num1) + " not found in list")
else:
    print("Item " + str(num1) + " found at index " + str(x))