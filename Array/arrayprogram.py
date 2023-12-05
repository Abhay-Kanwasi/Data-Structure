# Make a list using array

import ctypes
class Lists:

    def __init__(self):
        self.size = 1
        self.n = 0
        self.arr = self.__make_array(self.size)

    # len feature of list
    def __len__(self):
        return self.n 
    
    def append(self, item):
        # resize if the number of elements are equal to size of the array it means there is no spae in the array
        if self.n == self.size:
            self.__resize(self.size*2) # make the size double copy the elements from previous array
        # if there is space in the array
        self.arr[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        new_array = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content from old array to new array
        for i in range(self.n):
            new_array[i] = self.arr[i]
        # reassign A (because all the functionality is written for arr)
        self.arr = new_array

    # create a list
    def __make_array(self, capacactity):
        return (capacactity*ctypes.py_object)()
    
    def __str__(self):
        # print a list
        result = ''
        for i in range(self.n):
            result = result + str(self.arr[i]) + ','
        return '[' + result[:-1] + ']'
    
    def __getitem__(self, index):
        return

obj = Lists()

obj.append(2)
obj.append(2)
obj.append(2)

print(obj)