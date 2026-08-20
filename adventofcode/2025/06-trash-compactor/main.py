import re
from collections.abc import Callable
from functools import reduce
from operator import add, mul

Op = Callable[[int, int], int]

OPS: dict[str, Op] = {
    '+': add,
    '*': mul,
}


def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()

    rows, ops_line = lines[:-1], lines[-1]

    cols = zip(*(line.split() for line in rows))
    widths = [max(map(len, col)) for col in cols]

    rx = re.compile(' '.join(f'(.{{{w}}})' for w in widths))
    cells = [rx.match(line).groups() for line in rows]

    padded_columns = [list(col) for col in zip(*cells)]

    ops = [OPS[o] for o in ops_line.split()]

    return padded_columns, ops


def extract_numbers_from_padded(col: list[str]):
    return [int(''.join(ch)) for ch in zip(*col)]


def solve_1(cols: list[list[int]], ops: list[Op]):
    return sum(reduce(ops[i], map(int, col))
               for i, col in enumerate(cols))


def solve_2(cols: list[list[str]], ops: list[Op]):
    return sum(reduce(ops[i], extract_numbers_from_padded(col)) for i, col in enumerate(cols))


if __name__ == '__main__':
    columns, ops = parse_input('input.txt')

    print(f'Task 1: {solve_1(columns, ops)}')
    print(f'Task 2: {solve_2(columns, ops)}')
