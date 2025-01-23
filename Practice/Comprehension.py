# # Question 1
# """
#     Using list comprehension, write a program to generate a list of numbers in the range 2 to 50 that are dividable by 2 and 4.
# """
#
# divisible_list= [number for number in list(range(2,50)) if number % 4 == 0]
# # print(divisible_list)
#
#
# # Question 2
# """
#     Write a program to flattern the following list using list comprehension.
#     lists = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
# """
# """
# In programming, "flattening" can refer to converting a complex data structure (like a nested array or object) into a simpler, one-dimensional structure.
# """
#
# lists = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
# flattern_list = []
# # for item in lists:
# #     for number in item:
# #         flattern_list.append(number)
# # print(flattern_list)
#
#
# flattern_list = [number for item in lists for number in item]
# # print(flattern_list)
#
#
#
# # Question 3
# """
#     Write a program to add two 3 * 4 matrices using list comprehension.
# """
#
# matrice1 = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
# matrice2 = [[3, 4, 32, 44],[53, 63, 72, 87],[93, 108, 131, 112]]
# addition_matrice = []
# count = 0
#
# # for index in range(len(matrice1)):
# #     matrices = []
# #     for index2 in range(len(matrice1) + 1):
# #         matrice = matrice1[index][index2] + matrice2[index][index2]
# #         matrices.append(matrice)
# #     addition_matrice.append(matrices)-
#
# # list3 = [[4,6,35,48][58,69,79,95][103,118,142,124]]
#
# # addition_matrice = [[matrice1[index][index2] + matrice2[index][index2] for index2 in range(len(matrice1) + 1)] for index in range(len(matrice1))]
#
# # print(addition_matrice)
#
#
# # Question 4
# """
#     Write a program to create a set containing some randomly generated numbers in the range 15 to 45.
#     Count how many of these numbers are less than 30. Delete all numbers which are less than 30.
# """
#
# import random
# numbers_set = ()
# count = 0
# numbers = random.randint(15, 45)
#
# for number in numbers:
#     if number<30:
#         del number
#     else:
#         numbers_set.add(number)
#
#

# Creating a list of cubes of numbers
numbers = [1, 2, 3, 4, 5]
cubes = []

for number in numbers:
    cubes.append(number ** 3)

# Filtering odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

oddNum = [number for number in numbers if number % 2 == 1]
# for number in numbers:
#     if number % 2 != 0:
#         oddNum.append(number)
# print(f'oddNum {oddNum}')


# Find all the numbers from 1-1000 that are divisible by 7

DivisibleBy7 = [number for number in range(1, 1001) if number % 7 == 0]
# print(DivisibleBy7)

# Find all the numbers from 1-1000 that have a 3 in them

Have3 = [number for number in range(1, 1001) if '3' in str(number)]
for number in range(1, 1001):
    if '3' in str(number):
        Have3.append(number)

# print(Have3)

numbers_with_three = []
for i in range(1, 1001):
    num = i
    while num > 0:
        if num % 10 == 3:
            numbers_with_three.append(i)
            break
        num //= 10

# print(numbers_with_three)

# Count the number of spaces in a string


strings = 'This is my life'
contain_space = [string for string in strings if string == ' ']
# print(len(contain_space))


# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesterday they yodeled while eating yucky yams”
strings = "Yellow Yaks like yelling and yawning and yesterday they yodeled while eating yucky yams"
consonantsInStrings = [string for string in strings if string not in ['a', 'e', 'i', 'o', 'u', ' ']]
# print(consonantsInStrings)

# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)

demo_list = ['hi', 4, 8.99,'apple', ('t','b','n')]

pairs = [(index, value) for index, value in enumerate(demo_list)]
# print(pairs)


# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
CommonNumbers = [number for number in list_a if number in list_b]
# for number in list_a:
#     if number in list_b:
#         CommonNumbers.append(number)


# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
NumbersInSentence = [number for number in sentence.split(' ') if number.isnumeric()]
# for number in sentence.split(' '):
#     if number.isnumeric():
#         NumbersInSentence.append(number)

# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word
# ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’

oddOrEven = ['even' if number % 2 == 0 else 'odd' for number in range(20)]


# Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
MatchingNumbers = [(a,b) for a in list_a for b in list_b if a == b]
# CommonNum = ()
# for number in list_a:
#     if number in list_b:
#         CommonNum += (number,number)
#
# MatchingNumbers.append(CommonNum)
print(MatchingNumbers)


# Write a program to create a dictionary and add, update, and delete key-value pairs.
# def createDict():
#     dictionary = dict()
#     choice = int(input('please enter your choice/ 1.Add/ 2. Update/ 3. Delete/ 4. Exit'))
#
#     while True:
#         if(choice == 1):
#             key = input('please enter your key')
#             value =input('please enter your value')
#             dictionary[key] = value
#             print(f'{key} : {value}')
#         elif(choice == 2):
#             updateKey = input('please select the key to update it\'s value')
#             if(updateKey in dictionary):
#                 new_value = input('please enter the value that you want to update')
#                 dictionary[updateKey] = new_value
#                 print(f'{updateKey}:{new_value}')
#
#         elif(choice == 3):
#             deletekey = input('please select the key to delete')
#             if(deletekey in dictionary):
#                 dictionary[deletekey] = ''
#                 print(dictionary)
#         elif(choice == 4):
#             break
#
# print(createDict())

#
#
# # How do you iterate over keys, values, and key-value pairs in a dictionary? Provide examples.
# for key in dict.keys():
#     print(key)
# for values in dict.values():
#     print(values)
#
# for keys, values in dict.items():
#     print(keys,values)


# Write a program to merge two dictionaries.

dict_1 = {'a':1,'b':4,'c':6}
dict_2 = {'z':45,'x':78,'q':87}

dict_1.update(dict_2)
print(dict_1)



# What will happen if you try to access a key that doesn’t exist in a dictionary? How can you handle this?
## it will throw KeyError
# dict_1 = {'a':1,'b':4,'c':6}
# print(dict_1['d'])
dict_1 = {'a':1,'b':4,'c':6}
if 'd' in dict_1:
    print(dict_1['d'])
else:
    print('key not found')




