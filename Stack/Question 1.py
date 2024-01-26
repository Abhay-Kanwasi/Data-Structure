"""
Write a function in python that can reverse a string using stack data structure. 

reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW")
"""

from collections import deque

# 1. Direct Approch 


stack = deque()

def reverse_string(string):
    rstr = ''
    for char in string:
        stack.append(char)
        rstr = char + rstr
    print(rstr)
    
string = "We will conquere COVID-19"
reverse_string(string)



# 2. Object Oriented Approch

class Stack:

    # We create a container for deque which we use as stack
    def __init__(self):
        self.container = deque()
    
    # Now we create methods for our stack

    # 1. Push : In this we will add a value to the stack
    def Push(self,value):
        self.container.append(value)
    
    # 2. Pop : In this we delete the last element from the stack or you can say we pick out the last element.
    def Pop(self):
        return self.container.pop()
    
    # 3. Peek : In this we see the last item we added into stack.
    def Peek(self):
        return self.container[-1]
    
    # 4. Is_Empty : It will check whether the stack is empty or not.
    def Is_Empty(self):
        return len(self.container)==0
    
    # 5. Length : It will return the size of the stack.

    def Length(self):
        return len(self.container)


# Now we successfully created stack methods. 

# Now implement these to reverse the string.

def reverse(string):
    # Make an object for stack class. So we can use the methods we created above.
    stack = Stack()

    # This loop will push all the elements one by one to the stack container.
    for char in string:
        stack.Push(char)
    
    # We created a empty container here
    reverse_string = ''

    while stack.Length()!=0:
        reverse_string+=stack.Pop() # This will pop out the elements from the stack container in LIFO order.
    
    return reverse_string

if __name__ == '__main__':
    string = "We will conquere COVID-19"
    print(f"Orignal String : {string}")
    print(f"Reversed String : {reverse(string)}")



