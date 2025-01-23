'''
loops
set
tuple
dictionaries
list
lambda function
comprehension
'''

# Loop questions
# 1. Write a program to print the numbers from 1 to 10 using a for loop.
def printNum(start,end):
    for number in range(start,end+1):
       print(number)

# print(printNum(1,10))
# 2. What is the difference between for and while loops? Give an example of each.
# For Loop don't need any condition first to print a number or output where while loop runs based on condition which we define '

# 3. Write a program to calculate the factorial of a number using a while loop.
# 5*4*3
# facto = num * num - 1
def calculate_factorial(number):
    if number == 1:
        return 1
    else:
        factorial = 1
        while number > 1:
            factorial = factorial * number
            number = number - 1
        return factorial
# print(calculate_factorial(5))

# 4. How can you use the break and continue statements in loops? Provide examples.

def ExamplesBreakContinue(n):
    for number in range(1, n):
        if number == 10:
            continue
        print(number)
    return number # 1
ExamplesBreakContinue(20)


# 5. Iterate over a list of numbers and print only the even numbers using a loop.
def EvenNumbers(lst):
        for number in lst:
            if number % 2 == 0:
                print(number)
        return number
EvenNumbers([1,2,3,4,32,44,54,62,34,33])


# Dictionaries
# 1. Explain how a dictionary is different from a list.
# dict have key value pairs,, we can access any value by it's own unique key, instead list doesn't have any pairs or keys like dict.


# 2. Write a program to create a dictionary and add, update, and delete key-value pairs.
def CreateDict():
    keys = ('apple','banana','orange','mango')
    values = (30,40,20,10)
    dictn = dict(zip(keys,values))
    return dictn
print(CreateDict())
# 3. How do you iterate over keys, values, and key-value pairs in a dictionary? Provide examples.
# 4. Write a program to merge two dictionaries.
# 5. What will happen if you try to access a key that doesn’t exist in a dictionary? How can you handle this?




