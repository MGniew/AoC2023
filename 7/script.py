import sys


def get_hand_type(hand):
    set_hand = set(hand)
    if len(set_hand) == 5:
        return 0
    if len(set_hand) == 4:
        return 1
    if len(set_hand) == 3:
        if any([hand.count(c) == 3 for c in set(hand)]):
            return 3
        return 2
    if len(set_hand) == 2:
        if any([hand.count(c) == 4 for c in set(hand)]):
            return 5
        return 4
    return 6

def get_hand_type_with_jokers(hand):
    cards = "AKQT98765432J"
    if "J" not in hand or len(set(hand)) == 1:
        return get_hand_type(hand)

    return max(
        get_hand_type(hand.replace("J", card))
        for card in set(hand) - set("J")
    )


def solve_part1(hands):
    cards = "AKQJT98765432"
    key1=lambda hand: get_hand_type(hand)
    key2=lambda hand: [-cards.index(c) for c in hand]
    hands = sorted(hands, key=lambda hand: (key1(hand[0]), key2(hand[0])))
    return sum([i*int(h[1]) for i, h in enumerate(hands, start=1)])


def solve_part2(hands):
    cards = "AKQT98765432J"
    key1=lambda hand: get_hand_type_with_jokers(hand)
    key2=lambda hand: [-cards.index(c) for c in hand]
    hands = sorted(hands, key=lambda hand: (key1(hand[0]), key2(hand[0])))
    return sum([i*int(h[1]) for i, h in enumerate(hands, start=1)])


data = sys.stdin.read().splitlines()
data = [record.split() for record in data]
print(solve_part1(data))
print(solve_part2(data))







