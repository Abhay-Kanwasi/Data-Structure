
'''
    Condition : array or list must be in increasing/decreasing order.

    Algorithm (Asscending Order)

    Step 1 : Define the element you want to search as key
    Step 2 : start_index = 0, end_index = size of array - 1 
    Step 3 : Find the mid_element_index (start_index + end_index / 2 = mid element_index) # mid element must be an integer
    Step 4 : Start a loop with a condition that it will run till start_index <= end_index. Then inside loop
    Step 5 : If key == array[mid_element_index] # element found
    Step 6 : If key > array[mid_element_index] then start_index = mid_index + 1 
    Step 7 : If key < array[mid_element_index] then end_index = mid_index - 1
    Step 8 : Update you mid index because inside loop either start_index or end_index will be updated so also mid_index.        mid_index = int((start_index + end_index)/2) 
'''
def binary_search_ascending_order(arr, size, key):
    start = 0
    end = size - 1
    mid = int((start + end)/2)
    while start <= end:
        if key == arr[mid]:
            return f'Element found at index {mid}'
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = int((start + end)/2)
    return 'Element not found'
    

array = [2,4,6,8,9]
size = len(array)
key = 9

print(binary_search_ascending_order(array, size, key))

