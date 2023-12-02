from collections import Counter
from functools import reduce


MAX_CAPACITY = Counter({'red': 12, 'green': 13, 'blue': 14})


def parse_input(filename):
    games = []

    with open(filename, 'r+') as f:
        for line in f:
            if line == '\n':
                continue

            _, game = line.strip().split(': ')
            sets = game.split('; ')

            game_results = []

            for s in sets:
                game_set = Counter({'red': 0, 'green': 0, 'blue': 0})

                for cube in s.split(', '):
                    count, color = cube.split(' ')
                    game_set[color] = int(count)

                game_results.append(game_set)

            games.append(game_results)

    return games


def solve_1(games):
    return sum(
        game_id for game_id, game in enumerate(games, start=1)
        if all(game_set <= MAX_CAPACITY for game_set in game)
    )


def solve_2(games):
    selected_sets = [reduce(lambda a, b: a | b, sets) for sets in games]

    return sum(game['red'] * game['green'] * game['blue'] for game in selected_sets)


if __name__ == '__main__':
    games = parse_input('input.txt')

    print(f'Task 1: {solve_1(games)}')
    print(f'Task 2: {solve_2(games)}')
