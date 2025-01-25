import random

"""
loops
set
tuple
dictionaries
list
lambda function
comprehension
"""


# Loop questions
# 1. Write a program to print the numbers from 1 to 10 using a for loop.
def printNum(start, end):
    for number in range(start, end + 1):
        print(number)


# print(printNum(1,10))

# 2. What is the difference between for and while loops? Give an example of each. For Loop
# don't need any condition first to print a number or output where while loop runs based on condition which we define '

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
    number = 0
    for number in range(1, n):
        if number == 10:
            continue
        print(number)
    return number  # 1


# ExamplesBreakContinue(20)


# 5. Iterate over a list of numbers and print only the even numbers using a loop.
def EvenNumbers(lst):
    number = 0
    for number in lst:
        if number % 2 == 0:
            print(number)
    return number


# EvenNumbers([1,2,3,4,32,44,54,62,34,33])


# Dictionaries
# 1. Explain how a dictionary is different from a list.

# 2. Write a program to create a dictionary and add, update, and delete key-value pairs.
def CreateDict():
    keys = ('apple', 'banana', 'orange', 'mango')
    values = (30, 40, 20, 10)
    dictionary = dict(zip(keys, values))
    return dictionary


# Write a program to create a dictionary and add, update, and delete key-value pairs.
def createDict():
    dictionary = dict()
    choice = int(input('please enter your choice/ 1.Add/ 2. Update/ 3. Delete/ 4. Exit'))

    while True:
        if choice == 1:
            key = input('please enter your key')
            value = input('please enter your value')
            dictionary[key] = value
            print(f'{key} : {value}')
        elif choice == 2:
            updateKey = input('please select the key to update it\'s value')
            if updateKey in dictionary:
                new_value = input('please enter the value that you want to update')
                dictionary[updateKey] = new_value
                print(f'{updateKey}:{new_value}')

        elif choice == 3:
            delete = input('please select the key to delete')
            if delete in dictionary:
                dictionary[delete] = ''
                print(dictionary)
        elif choice == 4:
            break


# print(createDict())


# How do you iterate over keys, values, and key-value pairs in a dictionary? Provide examples.
"""
for key in dict.keys():
    print(key)
for values in dict.values():
    print(values)

for keys, values in dict.items():
    print(keys,values)
"""

# Write a program to merge two dictionaries.

dict_1 = {'a': 1, 'b': 4, 'c': 6}
dict_2 = {'z': 45, 'x': 78, 'q': 87}
dict_1.update(dict_2)
# print(dict_1)

# What will happen if you try to access a key that doesn’t exist in a dictionary? How can you handle this?
# it will throw KeyError
"""
dict_1 = {'a':1,'b':4,'c':6}
print(dict_1['d'])
dict_1 = {'a':1,'b':4,'c':6}
if 'd' in dict_1:
    print(dict_1['d'])
else:
    print('key not found')
"""

# LIST QUESTIONS

# Question 1 : Write a program to create a list of 5 odd integers. Replace the third element with a list of 4 even
# integers. Flatten, sort and print the list.

odd_integers = [1, 3, 5, 7, 9]
even_integers = [2, 4, 6, 8]
# odd_integers[2] = even_integers
odd_integers.extend(even_integers)
odd_integers.sort()

# Question 2 : Suppose a list contains 20 integers generated randomly. Receive a number from the keyboard and report
# position of all occurrences of this number in the list.

'''
random_list = [random.randint(1, 50) for i in range(20)]
print(random_list)

chosen_number = int(input('Enter the number:'))
position = [index for index, value in enumerate(random_list) if value == chosen_number]

if position:
    print(f'The number {chosen_number} is in the position(0 based indexing) {position}')
else:
    print(f'The number {chosen_number} is not found!!')
'''


# Question 3 : Write a Python program to check if each number is prime in a given list of numbers. Return True if all
# numbers are prime otherwise False.

def isPrime(provided_number):
    if provided_number == 1:
        return False
    elif provided_number == 2:
        return True
    else:
        for digit in range(2, provided_number):
            if provided_number % digit == 0:
                return False
        else:
            return True


primeOrNot = [3, 5, 25, 12, 17, 19]
for number in primeOrNot:
    print(isPrime(number))

