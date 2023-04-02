# Write a python program to get the number of occurrence of specific element of the array.

# Method 1
# array_list = [2, 3, 3, 1, 1, 1]
# element = int(input("Enter the number : "))
# occured = 0
# for i in array_list:
#     if i == element:
#         occured += 1
#
# print(f"{element} occurred {occured} times.")


# Method 2
from array import *

array_list = array('i', [2, 3, 3, 1, 1, 1])
item = 0
occurence = 0
element = int(input("Enter the number : "))
while item < len(array_list):
    if array_list[item] == element:
        occurence += 1
    item += 1
print(f"{element} occurred {occurence} times in the array.")

