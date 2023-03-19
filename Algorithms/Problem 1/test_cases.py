# 1. The quey occured in somewhere middle in the list.
test_case1 = []
test_case1.append({
    'input' : {
        'cards' : [13,11,10,8,7,5],
        'query' : 8
    },
    'output' : 3
})
test_case1.append({'cards' : [13,11,10,8,7,5]})
test_case1.append({'query': 8})
test_case1.append({'output' : 3})

# 2. query is the first element.
test_case2 = []
test_case2.append({
    'input' : {
        'cards' : [13,11,10,8,7,5],
        'query' : 13
    },
    'output' : 0
})
test_case2.append({'cards' : [13,11,10,8,7,5]})
test_case2.append({'query': 13})
test_case2.append({'output' : 0})

# 3. query is the last element.
test_case3 = []
test_case3.append({
    'input' : {
        'cards' : [13,11,10,8,7,5],
        'query' : 5
    },
    'output' : 5
})
test_case3.append({'cards' : [13,11,10,8,7,5]})
test_case3.append({'query': 5})
test_case3.append({'output' : 5})


# 4. The list of elements contains just one element which is query.
test_case4 = []
test_case4.append({
    'input' : {
        'cards' : [2],
        'query' : 2
    },
    'output' : 0
})
test_case4.append({'cards' : [2]})
test_case4.append({'query': 2})
test_case4.append({'output' : 0})

# 5. The list of elements doesn't contain query.
test_case5 = []
test_case5.append({
   'input' : {
    'cards' : [13,11,10,7],
    'query' : 2
   },
   'output' :  -1
})
test_case5.append({'cards' : [13,11,10]})
test_case5.append({'query': 2})
test_case5.append({'output' : -1})


# 6. The list of cards is empty.
test_case6 = []
test_case6.append({
    'input' : {
        'cards' : [],
        'query' : 2
    },
    'output' : -1
})
test_case6.append({'cards' : []})
test_case6.append({'query': 2})
test_case6.append({'output' : -1})


# 7. The list of cards contains repeted numbers.
test_case7 = []
test_case7.append({
    'input' : {
        'cards' : [13,12,12,12,11,7,7,6],
        'query' : 11
    },
    'output' : 4
})
test_case7.append({'cards' : [13,12,12,12,11,7,7,6]})
test_case7.append({'query': 11})
test_case7.append({'output' : 4})


# 8. The query occurs at more than one position in cards.
test_case8 = []
test_case8.append({
    'input' : {
        'cards' : [13,12,12,11,11,10,10,9,5,5,3],
        'query' : 5
    },
    'output' : 8
})
test_case8.append({'cards' : [13,12,12,11,11,10,10,9,5,5,3]})
test_case8.append({'query': 5})
test_case8.append({'output' : 8})



tests = []
tests.append(test_case1)
print(tests)


