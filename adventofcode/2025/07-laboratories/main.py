def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()

    return lines


def solve_1(lines: list[str]):
    state = [ch == 'S' for ch in lines[0]]
    lines = lines[1:]

    splits = 0

    for line in lines:
        for i, ch in enumerate(line):
            if state[i] and ch == '^':
                splits += 1
                state[i] = False

                if i > 0:
                    state[i - 1] = True

                if i + 1 < len(line):
                    state[i + 1] = True

    return splits


def solve_2(lines: list[str]):
    cache: dict[tuple[int, int], int] = {}

    def split(lines: list[str], line_number: int, pos: int) -> int:
        if (line_number, pos) in cache:
           return cache[(line_number, pos)]

        if line_number == len(lines) - 1:
            return 1

        line = lines[line_number]
        splits: int = 0

        if line[pos] == '.':
            splits += split(lines, line_number + 1, pos)

        if line[pos] == '^':
            if pos - 1 >= 0:
                splits += split(lines, line_number + 1, pos - 1)

            if pos + 1 < len(line):
                splits += split(lines, line_number + 1, pos + 1)

        cache[(line_number, pos)] = splits

        return splits

    pos = lines[0].index('S')
    lines = lines[1:]

    return split(lines, 0, pos)


if __name__ == '__main__':
    lines = parse_input('input.txt')

    print(f'Task 1: {solve_1(lines)}')
    print(f'Task 2: {solve_2(lines)}')
