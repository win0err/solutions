from collections import Counter


JOKER = 'J'

HAND_STRENGTHS = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]

CARD_STRENGTHS_JACK = '23456789TJQKA'
CARD_STRENGTHS_JOKER = 'J23456789TQKA'


def card_strengths(cards, strength):
    return [strength.index(c) for c in cards]


def hand_strength(cards):
    count = Counter(cards)
    hand_type = tuple(n for (_, n) in count.most_common())

    return HAND_STRENGTHS.index(hand_type)


def handle_joker(hand):
    if JOKER not in hand:
        return hand

    # non jokers or the strongest card
    available_cards = [c for c in hand if c != JOKER] or CARD_STRENGTHS_JOKER[-1:]
    best_card, _ = Counter(available_cards).most_common()[0]

    return hand.replace(JOKER, best_card)


def parse_input(filename):
    hands = []

    with open(filename, 'r+') as f:
        for line in f:
            hand, bid = line.split()

            hands.append((hand, int(bid)))

    return hands


def solve(hands, calc_strength_fn):
    hands = sorted([(calc_strength_fn(hand), bid) for hand, bid in hands])

    return sum(rank * bid for rank, (_, bid) in enumerate(hands, start=1))


def solve_1(hands):
    def calc_strength(hand):
        return hand_strength(hand), *card_strengths(hand, CARD_STRENGTHS_JACK)

    return solve(hands, calc_strength)


def solve_2(hands):
    def calc_strength(hand):
        new_hand = handle_joker(hand)
        return hand_strength(new_hand), *card_strengths(hand, CARD_STRENGTHS_JOKER)

    return solve(hands, calc_strength)


if __name__ == '__main__':
    hands = parse_input('input.txt')

    print(f'Task 1: {solve_1(hands)}')
    print(f'Task 2: {solve_2(hands)}')
