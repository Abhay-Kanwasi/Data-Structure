import array as arr
"""
1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.

2. Write a Python program to append a new item to the end of the array. 
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Append 11 at the end of the array:
New array: array('i', [1, 3, 5, 7, 9, 11])

3. Write a Python program to reverse the order of the items in the array. 
Sample Output
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Reverse the order of the items:
array('i', [3, 9, 1, 7, 3, 5, 3, 1])

4. Write a Python program to get the length in bytes of one array item in the internal representation.

5.Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents and also find the size of the memory buffer in bytes
"""

#Answer 1
print("Answer 1")

a = arr.array('i',[2,3,4,55,55])
print(a)
print("Total number of elements are : ",len(a))
num = int(input("How many element you want to access : "))
for i in range(num):
    print("index :",i,"element :",a[i])

print("\n")


#Answer 2
print("Answer 2")

simple = arr.array('i',[1,3,5,7,9])
print("Before appending :",simple)
num = int(input("Enter the number you want to append : "))
simple.append(num)
print("After appending :",simple)

print("\n")


#Answer 3
print("Answer 3")

orignal_array = arr.array('i',[1,3,5,7,9])
print("Before :",orignal_array)
orignal_array.reverse()
print("After :",orignal_array)

print("\n")


#Answer 4
print("Answer 4")


a = arr.array('i',[1,2,3,45,4,3,3])
print("Size of array in bytes :",a.itemsize)

print("\n")


#Answer 5
print("Answer 5")

a = arr.array('i',[1,2,3,4,5])
print("Buffer size :",a.buffer_info())

