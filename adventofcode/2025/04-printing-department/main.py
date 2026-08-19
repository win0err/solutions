from itertools import product


def parse_input(filename) -> list[list[str]]:
    with open(filename) as file:
        return [list(line.strip()) for line in file]


ROLL = '@'
EMPTY = '.'

NEIGHBOURS_DIFFS = [(dx, dy)
                    for dx, dy in product((-1, 0, 1), repeat=2)
                    if (dx, dy) != (0, 0)]


def get_cell(diagram: list[list[str]], x: int, y: int):
    if 0 <= y < len(diagram) and 0 <= x < len(diagram[y]):
        return diagram[y][x]

    return EMPTY


def count_rolls(diagram: list[list[str]], remove = False):
    diff = 0

    for y, _ in enumerate(diagram):
        for x, _ in enumerate(diagram[y]):
            if diagram[y][x] != ROLL:
                continue

            rolls_count = sum(get_cell(diagram, x + dx, y + dy) == ROLL
                              for dx, dy in NEIGHBOURS_DIFFS)

            if rolls_count < 4:
                diff += 1

                if remove:
                    diagram[y][x] = EMPTY

    return diff


def solve_1(diagram: list[list[str]]):
    return count_rolls(diagram)


def solve_2(diagram: list[list[str]]):
    total = 0

    while (diff := count_rolls(diagram, remove=True)):
        total += diff

    return total


if __name__ == '__main__':
    diagram = parse_input('input.txt')

    print(f'Task 1: {solve_1(diagram)}')
    print(f'Task 2: {solve_2(diagram)}')
