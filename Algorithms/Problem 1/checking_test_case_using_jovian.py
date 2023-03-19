from jovian_test_cases import tests
from jovian.pythondsa import evaluate_test_cases

def locate_cards(cards,query):
    position = 0
    while True:
        if cards[position] == query:
            return position
        position+=1
        if position == len(cards):
            return -1
        
evaluate_test_cases(locate_cards,tests)

