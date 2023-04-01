# Write a python program to reverse the order of the items in the array

arr = [2, 3, 8, 9]
print(f"Array before {arr}")


# Method 1
# arr_reverse = arr[::-1]
# print(f"Array after {arr_reverse}")


# Method 2
n = len(arr)
def reverse_arr(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
for i in range(5):
    print(arr[i])

