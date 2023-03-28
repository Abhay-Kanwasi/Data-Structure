# Linked List

A linked list is a data structure used to store a sequence of elements, where each element contains a value and a reference to the next element in the sequence. Unlike arrays, which store elements in contiguous memory locations, linked lists store elements in nodes that may be scattered throughout memory.
Example

Here's an example of what a linked list might look like in Python:

### python

> class Node:<br/>
    def __init__(self, value, next=None):<br/>
        self.value = value<br/>
        self.next = next<br/>
node4 = Node(4)<br/>
node3 = Node(3, node4)<br/>
node2 = Node(2, node3)<br/>
node1 = Node(1, node2)

head = node1  # The head of the linked list is the first node

In this example, we define a Node class that represents a node in a linked list. Each node has a value attribute and a next attribute that points to the next node in the sequence. We then create four nodes and link them together to create a linked list. The head variable points to the first node in the list.

## Traversing a Linked List

To traverse a linked list, you start at the first node and follow the references to the next node until you reach the end of the list. Here's an example of how to traverse the linked list we defined above:

### python

node = head  # Start at the first node
while node is not None:
    print(node.value)
    node = node.next

In this code, we set the node variable to the head of the linked list, and then use a while loop to iterate over each node in the list. We print the value of each node and update the node variable to point to the next node in the list until we reach the end (when node is None).