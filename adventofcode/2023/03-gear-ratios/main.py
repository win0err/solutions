from collections import defaultdict
from dataclasses import dataclass, field


NEIGBOURS_DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


@dataclass
class PartNumber:
    value: int = 0
    coords: tuple[int, int] = None
    adjacent_symbols: set[tuple[int, int]] = field(default_factory=set)


def parse_input(filename):
    part_numbers = []

    with open(filename, 'r+') as f:
        schematic = [line.strip() for line in f]

    max_x, max_y = len(schematic[0]) - 1, len(schematic) - 1

    def neighbours(x, y):
        return [
            (x + dx, y + dy) for (dx, dy) in NEIGBOURS_DELTA
            if 0 <= x + dx <= max_x and 0 <= y + dy <= max_y
        ]

    def is_symbol(char):
        return not char.isdigit() and char != '.'

    number = None

    for y, line in enumerate(schematic):
        for x, char in enumerate(line):
            if char.isdigit():
                if number is None:
                    number = PartNumber(coords=(x, y))

                number.value = number.value * 10 + int(char)

                number.adjacent_symbols.update(
                    ((nx, ny), schematic[ny][nx]) for (nx, ny) in neighbours(x, y)
                    if is_symbol(schematic[ny][nx])
                )

            if (x == max_x or not char.isdigit()) and number is not None:
                if len(number.adjacent_symbols) > 0:
                    part_numbers.append(number)

                number = None

    return part_numbers


def solve_1(part_numbers):
    return sum(pn.value for pn in part_numbers)


def solve_2(part_numbers):
    gears = defaultdict(list)

    for pn in part_numbers:
        for coords, symbol in pn.adjacent_symbols:
            if symbol == '*':
                gears[coords].append(pn)

    return sum(
        numbers[0].value * numbers[1].value for numbers in gears.values()
        if len(numbers) == 2
    )


if __name__ == '__main__':
    part_numbers = parse_input('input.txt')

    print(f'Task 1: {solve_1(part_numbers)}')
    print(f'Task 2: {solve_2(part_numbers)}')
