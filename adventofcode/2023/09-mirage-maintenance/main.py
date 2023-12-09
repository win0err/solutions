from itertools import pairwise


def parse_input(filename):
    sequences = []

    with open(filename, 'r+') as f:
        lines = f.read().strip().splitlines()
        sequences = [[int(n) for n in l.split()]for l in lines]

    return sequences


def extrapolate(sequence):
    extrapolated = sequence[-1]

    while not all(n == 0 for n in sequence):
        sequence = [b - a for a, b in pairwise(sequence)]
        extrapolated += sequence[-1]

    return extrapolated


def solve_1(sequences):
    return sum(extrapolate(seq) for seq in sequences)


def solve_2(sequences):
    return sum(extrapolate(seq[::-1]) for seq in sequences)


if __name__ == '__main__':
    sequences = parse_input('input.txt')

    print(f'Task 1: {solve_1(sequences)}')
    print(f'Task 2: {solve_2(sequences)}')
