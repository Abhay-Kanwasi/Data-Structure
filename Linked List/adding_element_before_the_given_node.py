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

    def add_begin(self,data):
        new_node = Node(data) # Now we succesfully created new node. We need to change the reference of the new node. for that 
        new_node.ref = self.head # Step 2 : New node will become the first node of the linked list.
        self.head = new_node # Step 3 : Point head to new node. Because now the first node of the linked list is new_node.

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

    def add_before(self,data,x):
        #In case linked list is empty
        if self.head is None:
            print("Linked list is empty.")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
            if n.ref is None:
                print("Node is not found.")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

LL1 = Linked_list()
LL1.add_begin(10)
LL1.add_before(20,10)
LL1.add_before(30,100)
LL1.print_LinkedList()

