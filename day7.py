# Day 7: Camel Cards (December 7th, 2023)

from collections import Counter
from utils import read_input
lines = read_input("day7.txt")

CARD_STRENGTH = {"J": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
HAND_STRENGTH = {"high_card": 1, "one_pair": 2, "two_pair": 3, "three_of_a_kind": 4, "full_house": 5, "four_of_a_kind": 6, "five_of_a_kind": 7} 

def type_of_hand(hand):
    hand_dict = dict(Counter(hand))
    values = set(hand_dict.values())

    if len(hand_dict.keys()) == 1:
        return "five_of_a_kind"
    elif (len(hand_dict.keys()) == 2) and (4 in values):
        return "four_of_a_kind"
    elif (len(hand_dict.keys()) == 2) and (3 in values):
        return "full_house"
    elif (len(hand_dict.keys()) == 3) and (3 in values):
        return "three_of_a_kind"
    elif (len(hand_dict.keys()) == 3) and (2 in values):
        return "two_pair"
    elif (len(hand_dict.keys()) == 4) and (2 in values):
        return "one_pair"
    elif (len(hand_dict.keys()) == 5):
        return "high_card"

def second_ordering(hands):
    alphabet = "23456789TJQKA"
    return sorted(hands, key=lambda word: [alphabet.index(c) for c in word])
    
def day7():
    result = 0
    bids = {}
    initial_sort = {"high_card": [], "one_pair": [], "two_pair": [], "three_of_a_kind": [], "full_house": [], "four_of_a_kind": [], "five_of_a_kind": []}

    for line in lines:
        hand, bid = line.split()
        bids[hand] = bid
        initial_sort[type_of_hand(hand)].append(hand)

    rank = 1
    values = initial_sort.values()
    for value in values:
        if len(value) == 1:
            result += rank * int(bids[value[0]])
            rank += 1
        if len(value) > 1:
            for hand in second_ordering(value):
                result += rank * int(bids[hand])
                rank += 1
    
    return result




    print(initial_sort)
    # for hand in initial_sort.values():



    # sort hands by rank

    # sort hands by type first 

    # do second ordering

    # create final 

print(type_of_hand("23456"))
print(day7())




