'''
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)

Serve Food: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
'''

# Direct Approch

import time # This will be used for managing order time
from collections import deque
import threading # This will help us to do tasks parllely

print("THIS IS A FOOD ORDERING SYSTEM")

buffer = deque() # Created instance of queue
def place_orders(orders):
    for order in orders:
        print(f"Placing the order for {order}.")
        buffer.appendleft(order) # Order will store in buffer in FIFO order.
        time.sleep(0.5)    

def serve_food():
    time.sleep(1)
    while True:
        # In case all the order will served we need to stop this loop or it will raise IndexError exception. For that we need to handle our exception.
        try:
            order = buffer.pop()
            print(f"Now serving {order}")
        except IndexError: 
            print("All the orders are served.")
            break
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_food)

    t1.start()
    t2.start()



# Object Oriented Approch

# from collections import deque
# import time 
# import threading

# # Created a queue with diffrent methods
# class Queue:
#     def __init__(self):
#         self.buffer = deque() 

#     def enqueue(self,value):
#         self.buffer.appendleft(value)
    
#     def dequeue(self):
#         return self.buffer.pop()
        
    
#     def is_empty(self):
#         return len(self.buffer)==0

#     def size(self):
#         return len(self.buffer)

# food_order_queue = Queue()

# def place_order(orders):
#     for order in orders:
#         print(f"Placing a order for {order}.")
#         food_order_queue.enqueue(order)
#         time.sleep(0.5)
    
# def serve_food():
#     time.sleep(1)
#     while True:
#         try:
#             order = food_order_queue.dequeue()
#             print(f"Now serving {order}")
#         except IndexError:
#             print("All the orders are served.")
#             break
#         time.sleep(2)
        

# if __name__ == '__main__':
#     orders = ['pizza','samosa','pasta','biryani','burger']
#     t1 = threading.Thread(target=place_order,args=(orders,))
#     t2 = threading.Thread(target=serve_food)

#     t1.start()
#     t2.start()

    
