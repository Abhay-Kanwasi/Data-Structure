# For implementing linked list we create data and refrence node. For that these are the steps:

# Step 1 : Create a node(with two parameters one is data and another one is reference)

class Node:
    def __init__(self,data): # We don't mention ref here because it is going to be None.
        self.data = data
        self.ref = None # Initially it is pointing to None(None means empty value.)

# Step 2 : For connecting nodes we create a class Linked List.
class LinkedList:
    def __init__(self): # Not take any parameter because initially head is none.
        self.head = None 
    
    def print_LinkedList(self): 
        # In this we talk about 2 senarios in the form of if and else.
        # Senario 1 : In the senario if Linked list is empty(How we know it is ? Simple if head is None(It means head doesn't point to any value or doesn't have any reference.))
        if self.head is None: 
            print("Linked list is empty.")

        # Senario 2 : In this senario if Linked list is not empty, It means it contains values(in the form of data and refrences).
        else:
            n = self.head        # Save the value of head into variable n
            while n is not None: # Untill n is not None (It means untill Linked list not empty do this..)
                print(n.data)    # Print the data.
                n = n.ref        # For shifting toward next node we do this n = n.ref 

LL1 = LinkedList() # Create an instance(LL1) of class LinkedList
LL1.print_LinkedList() # Using that instance call it's method print_LinkedList to print linked list.


# That's how we traverse in Linked List.
        