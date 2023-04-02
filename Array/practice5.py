# Write a python program to append items from inerrable to the end of the array

# Method 1
# from array import *
#
# items = array('i', [2, 3, 2, 1, 6])
# items.extend(items)
# print(items)


# Method 2
# array1 = [2, 3, 3, 1, 2]
# array2 = array1
# array3 = array1 + array2
# print(array3)

# Method 3
from array import *
array1 = array('i', [2, 3, 3, 1, 2])
array2 = array1
array3 = array1 + array2
print(array3)
