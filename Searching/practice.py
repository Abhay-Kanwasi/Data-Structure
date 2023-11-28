# Binary search for decreasing order

array = [9,8,7,5,3,2,1]
key = 0
size_of_array = len(array)

def binary_search_decreasing_order(array, key, size_of_array):
    start_index = 0
    end_index = size_of_array - 1
    mid_index = int((start_index + end_index)/2)
    while start_index <= end_index:
        if key == array[mid_index]:
            return f'Element found at {mid_index}'
        if key < array[mid_index]:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
        mid_index = int((start_index + end_index)/2)
    return 'Element not found'

print(binary_search_decreasing_order(array, key, size_of_array))