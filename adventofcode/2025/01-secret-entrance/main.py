def parse_input(filename):
    with open(filename) as file:
        return [-int(line[1:]) if line[0] == 'L' else int(line[1:]) for line in file.readlines()]


def solve_1(rotations: list[int]):
    dial = 50
    count = 0

    for rot in rotations:
        dial += rot
        dial %= 100

        if dial == 0:
            count += 1

    return count


if __name__ == '__main__':
    rotations = parse_input('input.txt')

    print(f'Task 1: {solve_1(rotations)}')
    print(f'Task 2: {0}')
