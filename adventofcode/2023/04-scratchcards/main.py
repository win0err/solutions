def parse_input(filename):
    cards = []

    with open(filename, 'r+') as f:
        for line in f:
            if line == '\n':
                continue

            _, numbers = line.strip().split(': ')
            numbers_have, numbers_win = map(
                lambda nums: set(int(n) for n in nums.split()),
                numbers.split(' | ')
            )

            matches = numbers_have & numbers_win
            cards.append(len(matches))

    return cards


def solve_1(cards):
    return sum(int(2**(matching_count - 1)) for matching_count in cards)


def solve_2(cards):
    cards_count = [1] * len(cards)

    for idx, matching_count in enumerate(cards):
        for i in range(matching_count):
            cards_count[idx + 1 + i] += cards_count[idx]

    return sum(cards_count)


if __name__ == '__main__':
    cards = parse_input('input.txt')

    print(f'Task 1: {solve_1(cards)}')
    print(f'Task 2: {solve_2(cards)}')
