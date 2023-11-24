"""
Time measurement techniques

1. Measuring time to execute 
- Not recommended because this is machine dependent but our goal is to measure algorithm time efficency so our goal make it machine independent.
- Time varies if implementation changes
- Different machines different time
- Does not work for extremely small input
- Time varies for different inputs, but can't establish a relationship


2. Counting operations involved
- Time varies if implementation changes
- No clear defination of which operation to count
- Time varies for different inputs and establish a relationship

3. Abstract notion of order of growth
Good to go method [Industry standard]
Basically it is BigO notation  



# sample problems

n^2 + 2n + 2 ==> O(n^2)
n^2 + 100000n + 3^1000 ==> O(n^2)
log(n) + n + 4 ==> O(n)
0.0001*n*log(n) + 300n ==> O(nlogn)
2n^30 + 3^n ==> O(3^n)


Types of orders of growth

-(rank 1)constant 
-(rank 2)logarithmic (in case of log) (sabse axa) (ex: binary search) (genrally when in a loop division operation is performed it is an log case) (input multiply and output add))
-(rank 3)linear (single loop) (ex: linear search)
-(rank 4)nlogn (merge sort) (input add and then output multiply)
-(rank 5)quadratic (in case of nested loops) (when two loops run same amount of time)
-(rank 6)exponential (opposite of logarithmic)


"""

import time 


def measuring_time_by_counting_operations1(a):
    return a*3 # operation count = 1

def measuring_time_by_counting_operations2(a):
    total = 0 # count = 1
    for i in range(a+1): # count = n
        total += i # count = 2 (total = total + i and a+1)
    return total
    # relationship | Time = 1 + 2x (where x is input)

def measuring_time_to_execute_using_for_loop():
    start_time = time.time()
    for i in range(1, 100):
        print(i)
    end_time = time.time()
    return end_time-start_time

# print(measuring_time_to_execute_using_for_loop())

def measuring_time_to_execute_using_while_loop():
    start_time = time.time()
    i = 0
    while i<100:
        print(i)
        i += 1
    end_time = time.time()
    return end_time-start_time

# print(measuring_time_to_execute_using_while_loop())


# 

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# n = 4
# for i in range(n+1):
    # print(fib(i))


def power(num):
    if num < 1:
        return 0
    elif num == 1:
        print(1)
        return 1
    else:
        prev = power(num//2)
        curr = prev*2
        print(curr)
        return curr

power(24)