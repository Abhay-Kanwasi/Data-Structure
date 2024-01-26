# Write a python program to append a new item to the end of the array

from array import *

arr = array('i', [2, 3, 4, 1])
print(f"Array is {arr}")

new = int(input("Enter the new number : "))
arr.append(new)
print(f"Array is {arr}")