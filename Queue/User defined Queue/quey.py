# Implementaion of Queue


# Approch 1 : Create a queue using list and trying to implement queue using list.

# queue = []
# def enqueue(element):
#     queue.append(element)

# def dequeue():
#     if not queue:
#         print("queue is empty.")
#     else:
#         e = queue.pop(0)
#         print("removed element : ",e)

# print("Operations\n1. Add element\n2. Delete element\n3. Display element\n4. Quit")
# while True:
#     choice = int(input("Enter your choice : "))
#     if choice == 1:
#         element = int(input("Enter the number : "))
#         enqueue(element)
#     elif choice == 2:
#         dequeue()
#     elif choice == 3:
#         print(queue)
#     elif choice == 4:
#         break
#     else:
#         print("Please enter a valid choice.\n")




# Approch 2 : Queuse implementation using modules

# 1. Using deque

# def enqueue(element):
#     queue.appendleft(element)

# def dequeue():
#     if not queue:
#         print("queue is empty.")
#     else:
#         e = queue.pop()
#         print("removed element : ",e)

# import collections
# queue = collections.deque()
# print("Operations\n1. Add element\n2. Delete element\n3. Display element\n4. Quit")
# while True:
#     choice = int(input("Enter your choice : "))
#     if choice == 1:
#         element = int(input("Enter the number : "))
#         enqueue(element)
#     elif choice == 2:
#         dequeue()
#     elif choice == 3:
#         print(queue)
#     elif choice == 4:
#         break
#     else:
#         print("Please enter a valid choice.\n")




# 2. Using Queue class
#  

