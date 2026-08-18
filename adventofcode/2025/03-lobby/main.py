def parse_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def find_joltage(number: str, count):
    assert count <= len(number) - 1

    result = ''
    start = 0

    for offset in range(count, 0, -1):
        window = number[start:len(number) - offset + 1]
        index = number.index(max(window), start)

        result += number[index]
        start = index + 1

    return int(result)


def solve_1(numbers: list[str]):
    return sum(find_joltage(n, 2) for n in numbers)


def solve_2(numbers: list[str]):
    return sum(find_joltage(n, 12) for n in numbers)


if __name__ == '__main__':
    numbers = parse_input('input.txt')

    print(f'Task 1: {solve_1(numbers)}')
    print(f'Task 2: {solve_2(numbers)}')
