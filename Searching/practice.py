# Find the peak element 

def find_peak_element(arr):
    start_index = 0
    end_index = len(arr)
    mid_index = int((start_index+end_index)/2)
    while start_index < end_index:
        if arr[mid_index] < arr[mid_index + 1]:
            start_index = mid_index + 1
        else:
            end_index = mid_index
        mid_index = int((start_index+end_index)/2)
    return arr[mid_index]

arr = [0, 3, 5, 12, 2]
print(find_peak_element(arr))