# Make a list using array

# We import ctypes, so we can use C language array to create python list
import ctypes


class Lists:

    def __init__(self):
        self.size = 1  # it will tell maximum items you can store
        self.n = 0  # it will tell how many items are stored currently

        # create a ctype array with size = self.size(__make_array)
        self.arr = self.__make_array(self.size)

    # LEN FEATURE OF LIST
    def __len__(self):  # triggered when len() is called
        return self.n

        # APPEND FEATURE OF LIST

    def append(self, item):
        # resize if the number of elements are equal to size of the array it means there is no spae in the array
        if self.n == self.size:
            self.__resize(self.size * 2)  # make the size double copy the elements from previous array
        # if there is space in the array
        self.arr[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        new_array = self.__make_array(new_capacity)
        self.size = new_capacity  # update the size of array
        # copy the content from old array to new array
        for i in range(self.n):
            new_array[i] = self.arr[i]
        # reassign A (because all the functionality is written for arr)
        self.arr = new_array

    # CREATE FEATURE OF LIST
    def __make_array(self, capacity):
        """
        create a C type array(fixed array/ static size) also it's a referential array(you can store multiple type of
        data) with size capacity
        """
        return (capacity * ctypes.py_object)()

    # PRINT FEATURE OF LIST
    def __str__(self):  # this triggers when print is called
        # print a list
        result = ''
        for i in range(self.n):
            result = result + str(self.arr[i]) + ','
        return '[' + result[:-1] + ']'

    # INDEX FEATURE OF LIST
    def __getitem__(self, index):  # this method triggered when user put [] after object
        if 0 <= index < self.n:
            return self.arr[index]
        else:
            raise IndexError('Index out of range')

    #   DELETE FUNCTIONALITY OF LIST

    def __delitem__(self, index):
        if 0 <= index < self.n:
            for i in range(index, self.n - 1):  # shifting the values
                self.arr[i] = self.arr[i + 1]

            self.n = self.n - 1  # because one element get deleted the array will decrease by 1
        else:
            raise ValueError('Index out of range')

    # POP FEATURE OF LIST

    def pop(self):
        if self.n == 0:
            raise IndexError('Index out of range')
        print(self.arr[self.n - 1])
        self.n = self.n - 1

    # CLEAR FUNCTIONALITY OF LIST

    def clear(self):
        self.n = 0
        self.size = 1

    # FIND FUNCTIONALITY OF LIST

    def find(self, item):
        for value in range(self.n):
            if self.arr[value] == item:
                return value
        return ValueError('Item not found')

    # INSERT FUNCTIONALITY OF LIST

    def insert(self, index, item):
        if self.n == self.size:  # check if space is available or not
            self.__resize(self.size * 2)  # if it is then resize the array

        for i in range(self.n, index, -1):  # for shift the values(we insert to a specific index, so we have to shift
            # values
            self.arr[i] = self.arr[i - 1]

        self.arr[index] = item  # insert the item at the index
        self.n = self.n + 1  # because a new item is added so the size of the array will increase by 1

    #   REMOVE FUNCTIONALITY OF LIST

    def remove(self, item):
        index = self.find(item)

        if int == type(index):
            self.__delitem__(index)
        else:
            return index


list_obj = Lists()

list_obj.append(2)
list_obj.append(2.3)
list_obj.append(4)
print("append functionality")

del list_obj[0]
print("delete functionality using del")

list_obj.remove(2)
print("remove functionality using remove")

list_obj.pop()
print("remove last item functionality using pop")

list_obj.insert(2, 12)
print("insert functionality using insert")

item = list_obj.find(2)
print("find the item functionality using find", item)

list_obj.clear()
print("clear functionality using clear")

print(list_obj)
