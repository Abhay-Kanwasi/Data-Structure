# Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

# Step 1 : State the problem clearly. Identify inputs and outputs.

# We need to write a python program to find the position of a given number that arranged in decreasing order. We also need to minimize the number of times we access elements from the list.



# Step 2 : Come up with some example inputs & outputs. Try to cover all edge cases. 

# Examples 
# def locate_card(cards,query):
#     pass
# test = {
#     'input' : {
#         'cards' : [13,11, 10, 7, 4, 3, 1, 0],
#         'query' : 7
#     },
#     'output' : 7
# }

# locate_card(**test['input']) == test['output']


# Edge Cases
"""
1. The query occured in somewhere middle in the list.
2. query is the first element.
3. query is the last element.
4. The list of elements contains just one element which is query.
5. The list of elements doesn't contain query.
6. The list of cards is empty.
7. The list of cards contains repeted numbers.
8. The query occurs at more than one position in cards.
9. """
# => Check test_cases.py for codes of edge cases.

