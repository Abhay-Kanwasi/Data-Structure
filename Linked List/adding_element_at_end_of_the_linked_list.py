# For adding element at the end of the linked list

class Node: # Step 1 : Create a node.
    def __init__(self,data):     # We don't mention ref here because it is going to be None.
        self.data = data
        self.ref = None          # Initially it is pointing to None(None means empty value.)

class Linked_list:
    def __init__(self):
        self.head = None
    
    def print_LinkedList(self):  # This taken from traverse_singly_linked_list.

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
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:    # In case if Linked list is empty
            self.head = new_node # Then it we just point head to new_node.(head contain ref of new node)
        else:
            n = self.head        # initially we take n and store head value into it
            # Now we want to go at the end of the linked list.
            while n.ref is not None: # Untill refrence become NULL we keep moving to next refrence
                n = n.ref
            n.ref = new_node     # Whenever it happens we will point that refrence to new_node(or you can say it will now point to new_node instead of NULL.)
        
LL1 = Linked_list()
LL1.add_end(19)
LL1.add_end(22)
LL1.print_LinkedList()            # This will print as ordered we add values because we are adding it at the end of the linked list.

    



