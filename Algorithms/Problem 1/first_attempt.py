from test_cases import test_case1,test_case2,test_case3
def locate_cards(cards,query):
    position = 0
    while True:
        if cards[position] == query:
            return position
        position+=1
        if position == len(cards):
            return -1
        
# print(test_case1[1]['cards'])
# print(test_case1[2]['query'])
# print(test_case1[3]['output'])

# Test_case1
locate_card_output_1 = locate_cards(test_case1[1]['cards'],test_case1[2]['query'])
test_case1_output = test_case1[3]['output'] 
if locate_card_output_1 == test_case1_output:
    print("test_case1 : Passed")
else:
    print("test_case1 : Failed")

# Test_case2
locate_card_output_2 = locate_cards(test_case2[1]['cards'],test_case2[2]['query'])
test_case2_output = test_case2[3]['output']
if locate_card_output_2 == test_case2_output:
    print("test_case2 : Passed")
else:
    print("test_case2 : Failed")

# Test_case3
locate_card_output_3 = locate_cards(test_case3[1]['cards'],test_case3[2]['query'])
test_case3_output = test_case3[3]['output']
if locate_card_output_3 == test_case3_output:
    print("test_case3 : Passed")
else:
    print("test_case3 : Failed")
