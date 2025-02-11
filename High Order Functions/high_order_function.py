# functions : first class values

"""
    lambda functions: Normal functions have names like we use def keyword. lambda functions do not have name, and they defined using lambda keyword. lambda functions are commonly used for short functions that are convenient to define at the point where they are called or you can say that there will be less reusablity and adjust in function. lamda functions are also called anonymous functions or inline functions.

    A lambda function can take any number of arguments but can return only one value.
    Syntax: lambda argument: expression (':' separates the parameters to be passed to the lambda function)
"""

# lambda argument: expression

# High Order Functions
# A high order function is a function that can receive other functions as argument or return them.
# 3 high order function: map, filter, reduce

# Map: operation applies a function to each element in the sequence like list, tuple etc return sequence containing the results.
# Values of input = Values of output
# Example : Finding square root of all numbers in the list and returning a list of these roots.

# Filter: operation applies a function to all element in the sequence. a sequence of those elements for which the function returns True
# Example: Checking whether each element in a list is an alphabet and returning a list of alphabet

# Reduce: operation performs a rolling computation to sequential pairs of values in a sequence and returns a result.
# Example Concatenating all strings in a list and returning the final string.


# Map() function
list1 = [1, 2, 3, 4, 5]
list2 = map(lambda number: number * number, list1)  # map(function_to_apply, list_of_inputs)


# print(list(list2))

# Filter() function
def function(number):
    if number % 2 == 0:
        return True
    else:
        return False


list2 = ['1', 'A', 'C', '4', '5']
list3 = filter(str.isalpha, list2)
# print(list(list3))


# reduce
from functools import reduce


def getsum(x, y):
    return x + y


list4 = [2, 4, 6]
some = reduce(getsum, list4)  # ((2 + 4) + 6) => 6 + 6 = 12
print(some)
