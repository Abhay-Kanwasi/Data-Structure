# Linked List

A linked list is a data structure used to store a sequence of elements, where each element contains a value and a reference to the next element in the sequence. Unlike arrays, which store elements in contiguous memory locations, linked lists store elements in nodes that may be scattered throughout memory.

    |node 1|--->|node 2|--->|node 3|--->|node 4|

<br />

### Another Definition  

It is a linear data structure made up of chain of nodes in which each node contains a data field and a link or reference of next node.

      |data|next node link|

So we can say linked list is chain of nodes. It can contain data field and only one link(link of next node).

In another case it can contain data field and two links. One is previous node link and second on eis next node link. 

       |previous node link|<----|data|---->|next node link| 
<br />

###  Head and Tail
`Head :` Starting point of each linked list is the reference to the first node is called Head/front.

`Tail :` And the last node is called Tail which normally points to null.

<br />

### Advantages

- Dynamic memory allocation
- Element can insert and delete form any position.
- You can use linked list to implement stack, queue, graph.
- Linked list are used to represent and manipulate polynomials(Mathematical expression(e.g. x^2 + y^2 + 2)).

### Disadvantage

- Each node contains 2 entities, so it needs extra memory.
- No elements can be accessed randomly.

### Implementation

- Web browser go to previous or next page.
- Music player : songs are linked.
- Image Viewer : image are linked.

### Types of linked list

- Singly linked list
- Doubly linked list
- Circular linked list

#### Singly Linked List
If each node of the linked list contains only one link that is the link of the next node. Then that is called singly linked list.

    1010(Head)     1074         1121         1134
    |10|1074|--->|20|1121|--->|30|1134|--->|40|null|

It is the most commonly used linked list. It allows you to go in forward direction only going backward is not easy. Because each node knows it's next node where is present, but it doesn't know about its previous node.


Example

Here's an example of what a linked list might look like in Python:

#### Code

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