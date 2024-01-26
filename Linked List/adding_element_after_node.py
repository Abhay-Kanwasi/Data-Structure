# For adding element after the given node of the linked list

class Node: 
    def __init__(self,data):     
        self.data = data
        self.ref = None          

class Linked_list:
    def __init__(self):
        self.head = None
    
    def print_LinkedList(self): 
        if self.head is None: 
            print("Linked list is empty.")
        else:
            n = self.head        # Save the value of head into variable n
            while n is not None: # Untill n is not None (It means untill Linked list not empty do this..)
                print(n.data,"---->",end=" ")    # Print the data.
                n = n.ref       
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:    # In case if Linked list is empty
            self.head = new_node # Then it we just point head to new_node.(head contain ref of new node)
        else:
            n = self.head       
            while n.ref is not None: 
                n = n.ref
            n.ref = new_node    
        
    def add_after(self,data,x):
        n = self.head
        # First find the node which after we want to add new node.
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked List.")
        # After finding the node 
        else:
            new_node = Node(data)  # Create the new node using Node class
            new_node.ref = n.ref   # In new_node refrence now store the refrence of next node.
            n.ref = new_node       # Now selected node refrence store the refrece of new node.

LL1 = Linked_list()
LL1.add_end(19)
LL1.add_end(22)
LL1.add_end(100)

# You can add new node after any node just first give the value of node and then give the value after which you want to add value(node)
 
#LL1.add_after(200,19) # After 19
LL1.add_after(200,100) # After 100

LL1.print_LinkedList()            
# This will print as ordered we add values because we are adding it at the end of the linked list.

    






