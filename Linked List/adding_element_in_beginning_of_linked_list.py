# For implementing insertion of element in Linked List follow these steps..


# 1. For adding element at the beginning of the linked list.

class Node: # Step 1 : Create a node.
    def __init__(self,data): # We don't mention ref here because it is going to be None.
        self.data = data
        self.ref = None # Initially it is pointing to None(None means empty value.)

class Linked_list:
    def __init__(self):
        self.head = None
    
    def print_LinkedList(self): # This taken from traverse_singly_linked_list.

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
    
    def add_begin(self,data):
        new_node = Node(data) # Now we succesfully created new node. We need to change the reference of the new node. for that 
        new_node.ref = self.head # Step 2 : New node will become the first node of the linked list.
        self.head = new_node # Step 3 : Point head to new node. Because now the first node of the linked list is new_node.

LL1 = Linked_list() # Created a instance of class Linked List.
LL1.add_begin(10)
LL1.add_begin(20)
LL1.print_LinkedList() # We want to check this is working or not.

# It will print before adding 10 Linked List is empty now we succesfully added 20 and 10. (first it will print 20 because we are adding elements at the beginning.)






     