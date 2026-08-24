from collections import Counter


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

                for j in (i + 1, i - 1):
                    if 0 <= j < len(line):
                        state[j] = True

    return splits


def solve_2(lines: list[str]):
    state = Counter({lines[0].index('S'): 1})

    for line in lines[1:]:
        new_state: Counter[int] = Counter()

        for i, n in state.items():
            if line[i] == '^':
                for j in (i + 1, i - 1):
                    if 0 <= j < len(line):
                        new_state[j] += n

            if line[i] == '.':
                new_state[i] += n

        state = new_state

    return sum(state.values())


if __name__ == '__main__':
    lines = parse_input('input.txt')

    print(f'Task 1: {solve_1(lines)}')
    print(f'Task 2: {solve_2(lines)}')
