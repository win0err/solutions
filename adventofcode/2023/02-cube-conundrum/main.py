from collections import Counter


MAX_CAPACITY = Counter({'red': 12, 'green': 13, 'blue': 14})


def parse_input(filename):
    games = []

    with open(filename, 'r+') as f:
        for line in f:
            if line == '\n':
                continue

            _, game = line.strip().split(': ')
            sets = game.split('; ')

            best_set = Counter()

            for s in sets:
                for v in s.split(', '):
                    count, color = v.split()
                    best_set[color] = max(int(count), best_set[color])

            games.append(best_set)

    return games


def solve_1(games):
    return sum(
        game_id for game_id, best_set in enumerate(games, start=1)
        if best_set <= MAX_CAPACITY
    )


def solve_2(games):
    return sum(s['red'] * s['green'] * s['blue'] for s in games)


if __name__ == '__main__':
    games = parse_input('input.txt')

    print(f'Task 1: {solve_1(games)}')
    print(f'Task 2: {solve_2(games)}')
