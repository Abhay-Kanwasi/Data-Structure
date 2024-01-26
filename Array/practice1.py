#1 Write an python program to create an array of 5 integers and display the array items. Access individual elements through indexes.

arr = []
for i in range(5):
    a = int(input("Enter the nubmer : "))
    arr.append(a)
print(f"The array is : {arr}")
index = int(input("Enter the index of the number : "))
print(arr[index])