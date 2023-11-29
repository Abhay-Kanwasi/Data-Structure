# Question 1 : In an sorted array you have to find first and last occurence of a element. Duplicate elements are allowed. You have size of array and element you have to find

''' 1
We want left most occurence of the element because that will be the first occurence of the number. After every succesful iteration we have to search in left part after every succesful iteration 
'''

def first_occurence(arr, key, size):
    start_index = 0
    end_index = size - 1
    mid_index = int((start_index + end_index)/2)
    ans = -1
    while start_index <= end_index:
        if key == arr[mid_index]:
            ans = mid_index
            end_index = mid_index - 1 # that why #1
        elif key < arr[mid_index]:
            end_index = mid_index - 1
        elif key > arr[mid_index]:
            start_index = mid_index + 1
        mid_index = int((start_index + end_index)/2)
    return ans

def last_occurence(arr, key, size):
    start_index = 0
    end_index = size - 1
    mid_index = int((start_index + end_index)/2)
    ans = -1
    while start_index <= end_index:
        if key == arr[mid_index]:
            ans = mid_index
            start_index = mid_index + 1 # that why #1
        elif key < arr[mid_index]:
            end_index = mid_index - 1
        elif key > arr[mid_index]:
            start_index = mid_index + 1
        mid_index = int((start_index + end_index)/2)
    return ans


key = 7
arr = [2,4,4,7,7,7,7,7,7,7,8,9]
size = len(arr)

def first_last_position():
    first = first_occurence(arr, key, size)
    last = last_occurence(arr, key, size)
    pair_ = (first, last)
    return pair_

# print(first_last_position())




''' Question 2 
key = 7
arr = [2,4,4,7,7,7,7,7,7,7,8,9]
size = len(arr)
Find the occurence of 7 

It's a trick question : Always remember it's a ordered array(ascending/descending) whenever we have first and last occurence there is no other number between them it's only one number because it's a ascending array that's why it's simple to find the occurence. [number_of_occurence = (end_occurence - firsts_occurence) + 1]
'''

def occurence(key):
    number_of_occurence = (last_occurence(arr, key, size) - first_occurence(arr, key, size)) + 1
    return number_of_occurence

# print(occurence(7))



'''
# Question 3 : Peak index in a mountain array
'''
