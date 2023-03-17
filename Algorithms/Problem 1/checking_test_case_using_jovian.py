def locate_cards(cards,query):
    position = 0
    while True:
        if cards[position] == query:
            return position
        position+=1
        if position == len(cards):
            return -1
from test_cases import test_case1
from jovian.pythondsa import evaluate_test_case
evaluate_test_case(locate_cards,test_case1[0])