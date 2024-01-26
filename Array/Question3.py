import array as arr


one_dimensional_array = arr.array('i', [])
max_size = int(input("Enter the maximum size of the array : "))

for element in range(max_size):
    number = int(input("Enter the number : "))
    one_dimensional_array.append(number)

for i in range(len(one_dimensional_array)):
    number = int(input("What number you want to find : "))
    if one_dimensional_array[i] == number:
        print(f"Number found at index {i}")
        