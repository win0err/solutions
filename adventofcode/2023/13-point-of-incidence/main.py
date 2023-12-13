def parse_input(filename):
    patterns = []

    with open(filename, 'r+') as f:
        patterns = f.read().strip().split('\n\n')
        patterns = [pattern.splitlines() for pattern in patterns]

    return patterns


def find_reflection(pattern, allowed_diff=0):
    fold_lines = range(1, len(pattern))

    for pos in fold_lines:
        l, r = pattern[:pos][::-1], pattern[pos:]

        diff = 0
        for lines in zip(l, r):
            diff += sum(lchar != rchar for lchar, rchar in zip(*lines))

        if diff == allowed_diff:
            return pos

    return 0


def solve(patterns, allowed_diff):
    total = 0

    for rows in patterns:
        total += find_reflection(rows, allowed_diff)*100

        cols = list(zip(*rows))
        total += find_reflection(cols, allowed_diff)

    return total


def solve_1(patterns):
    return solve(patterns, 0)


def solve_2(patterns):
    return solve(patterns, 1)


if __name__ == '__main__':
    patterns = parse_input('input.txt')

    print(f'Task 1: {solve_1(patterns)}')
    print(f'Task 2: {solve_2(patterns)}')
