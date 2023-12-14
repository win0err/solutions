ROCK_ROUNDED = 'O'
ROCK_CUBIC = '#'
EMPTY_SPACE = '.'


def parse_input(filename):
    rows = []

    with open(filename, 'r+') as f:
        rows = f.read().strip().splitlines()

    return rows


def tilt_line(line):
    line = [ch for ch in line]

    empty_idx = line.index(EMPTY_SPACE)
    idx = empty_idx + 1

    try:
        while idx < len(line):
            if line[idx] == ROCK_ROUNDED:
                line[idx], line[empty_idx] = EMPTY_SPACE, ROCK_ROUNDED

                while line[empty_idx] != EMPTY_SPACE:
                    empty_idx += 1

                idx = empty_idx + 1

            elif line[idx] == ROCK_CUBIC:
                empty_idx = idx + 1

                while line[empty_idx] != EMPTY_SPACE:
                    empty_idx += 1

                idx = empty_idx + 1

            elif line[idx] == EMPTY_SPACE:
                while line[idx] == EMPTY_SPACE:
                    idx += 1

    except IndexError:
        pass  # done

    return line


def tilt_matrix(matrix):
    return [tilt_line(line) for line in matrix]


def calc_load(matrix):
    total = 0

    for line in matrix:
        loads = reversed(range(1, len(line)+1))
        total += sum(load for load, rock in zip(loads, line)
                     if rock == ROCK_ROUNDED)

    return total


def rotate(matrix, clockwise=True):
    if clockwise:
        rotated = list(list(col[::-1]) for col in zip(*matrix))
    else:
        rotated = list(list(col) for col in zip(*matrix))[::-1]

    return rotated


def serialize(matrix):
    return '\n'.join(''.join(col) for col in matrix)


def solve_1(matrix):
    matrix = tilt_matrix(matrix)
    return calc_load(matrix)


def solve_2(matrix):
    last_seen_at = {}
    iteration = 0

    ITERATIONS = 1_000_000_000

    while iteration < ITERATIONS:
        serialized = serialize(matrix)

        if serialized in last_seen_at:
            interval = iteration - last_seen_at[serialized]
            count = (ITERATIONS - iteration) // interval

            iteration += interval * count

        last_seen_at[serialized] = iteration

        for _ in range(4):
            matrix = tilt_matrix(matrix)
            matrix = rotate(matrix)

        iteration += 1

    return calc_load(matrix)


if __name__ == '__main__':
    matrix = parse_input('input.txt')
    matrix = rotate(matrix, clockwise=False)  # initial position

    print(f'Task 1: {solve_1(matrix)}')
    print(f'Task 2: {solve_2(matrix)}')
