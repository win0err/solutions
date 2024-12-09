from operator import add, mul
from functools import cache


def concat(a, b):
    return int(f'{a}{b}')


def parse_input(filename):
    equations = []

    with open(filename, 'r+') as file:
        for line in file:
            if line == '':
                continue

            res, nums = line.split(':')

            res = int(res)
            nums = [int(n) for n in nums.split()]

            equations.append((res, nums))

    return equations


@cache
def generate_operators(length, concat_enabled=False):
    def gen(remaining, current = []):
        if remaining == 0:
            results.append(current)

            return

        gen(remaining - 1, [*current, add])
        gen(remaining - 1, [*current, mul])

        if concat_enabled:
            gen(remaining - 1, [*current, concat])

    results = []
    gen(length)

    return results


def solve(equations, concat_enabled):
    result = 0

    for equation in equations:
        expected, numbers = equation

        for operators in generate_operators(len(numbers) - 1, concat_enabled):
            actual = numbers[0]

            for i, op in enumerate(operators, start=1):
                actual = op(actual, numbers[i])

                if actual > expected:
                    break

            if actual == expected:
                result += expected

                break

    return result


if __name__ == '__main__':
    equations = parse_input('input.txt')

    print(f'Task 1: {solve(equations, concat_enabled=False)}')
    print(f'Task 2: {solve(equations, concat_enabled=True)}')
