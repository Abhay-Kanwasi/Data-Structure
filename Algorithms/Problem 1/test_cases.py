tests = []
# The quey occured in somewhere middle in the list.
tests.append({
    'input' : {
        'cards' : [13,11,10,8,7,5],
        'query' : 8
    },
    'output' : 3
})

# 2. query is the first element.
tests.append({
    'input' : {
        'cards' : [13,11,10,8,7,5],
        'query' : 13
    },
    'output' : 0
})

# 3. query is the last element.
tests.append({
    'input' : {
        'cards' : [13,11,10,8,7,5],
        'query' : 5
    },
    'output' : 5
})

# 4. The list of elements contains just one element which is query.
tests.append({
    'input' : {
        'cards' : [2],
        'query' : 2
    },
    'output' : 0
})

# 5. The list of elements doesn't contain query.
tests.append({
   'input' : {
    'cards' : [13,11,10,7],
    'query' : 2
   },
   'output' :  -1
})

# 6. The list of cards is empty.
tests.append({
    'input' : {
        'cards' : [],
        'query' : 2
    },
    'output' : -1
})

# 7. The list of cards contains repeted numbers.
tests.append({
    'input' : {
        'cards' : [13,12,12,12,11,7,7,6],
        'query' : 11
    },
    'output' : 4
})

# 8. The query occurs at more than one position in cards.
tests.append({
    'input' : {
        'cards' : [13,12,12,11,11,10,10,9,5,5,3],
        'query' : 5
    },
    'output' : 8
})

print(tests)






