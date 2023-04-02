# Write a python program to reverse the order of the items in the array

arr = [2, 3, 8, 9]
print(f"Array before {arr}")

# Method 1
arr_reverse = arr[::-1]
print(f"Array after {arr_reverse}")


# Method 2
reversed = []
for value in arr:
    reversed = [value] + reversed
print(reversed)


# Method 3


