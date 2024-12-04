from collections import deque, Counter

X = 'X'
M = 'M'
A = 'A'
S = 'S'

XMAS = {
    X: M,
    M: A,
    A: S,
    S: None,
}

DIAGONAL_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
ALL_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)] + DIAGONAL_DIRECTIONS


def parse_input(filename):
    with open(filename, 'r+') as file:
        return list(list(line.strip()) for line in file if line != '')


def count_all_xmas_from_x(matrix, x_point):
    size = len(matrix)

    sx, sy = x_point
    if matrix[sy][sx] == S:
        raise Exception("Starting point must be X")

    queue = deque((x_point, direction) for direction in ALL_DIRECTIONS)
    count = 0

    while queue:
        point, direction = queue.popleft()

        x, y = point
        dx, dy = direction

        # found
        if matrix[y][x] == S:
            count += 1
            continue

        nx, ny = x + dx, y + dy

        # X should lead to M, M to A, A to S
        if 0 <= ny < size and 0 <= nx < size and matrix[ny][nx] == XMAS.get(matrix[y][x], None):
            queue.append(((nx, ny), direction))

    return count


def solve_1(matrix):
    size = len(matrix)

    xmas_count = 0
    for y in range(size):
        for x in range(size):
            if matrix[y][x] == X:
                xmas_count += count_all_xmas_from_x(matrix, (x, y))

    return xmas_count


def solve_2(matrix):
    size = len(matrix)

    xmas_count = 0
    for y in range(1, size - 1):
        for x in range(1, size - 1):

            if matrix[y][x] == A:
                neighbours = Counter(matrix[y + dy][x + dx] for dx, dy in DIAGONAL_DIRECTIONS)

                # found 2 x S and 2 x M on edges except MAM and SAS
                if neighbours.get(M) == 2 and neighbours.get(S) == 2 \
                   and matrix[y + 1][x + 1] != matrix[y - 1][x - 1]:
                    xmas_count += 1

    return xmas_count


if __name__ == '__main__':
    matrix = parse_input('input.txt')

    print(f'Task 1: {solve_1(matrix)}')
    print(f'Task 2: {solve_2(matrix)}')
