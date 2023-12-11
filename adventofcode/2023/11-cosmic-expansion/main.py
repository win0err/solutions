from itertools import combinations


EMPTY_SPACE = '.'
GALAXY = '#'


def parse_input(filename):
    matrix = []

    with open(filename, 'r+') as f:
        matrix = f.read().strip().splitlines()

    return matrix


def count_voids(rows):

    cols = list(zip(*rows))
    w, h = len(cols), len(rows)

    voids_at_x = [0] * w
    count = 0
    for x, col in enumerate(cols):
        voids_at_x[x] = count

        if all(ch == EMPTY_SPACE for ch in col):
            count += 1


    voids_at_y = [0] * h
    count = 0
    for y, row in enumerate(rows):
        voids_at_y[y] = count

        if all(ch == EMPTY_SPACE for ch in row):
            count += 1

    return voids_at_x, voids_at_y


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(matrix, expansion):
    extra = expansion - 1  # 1 existing void + n-1 extra voids

    w, h = len(matrix[0]), len(matrix)
    voids_at_x, voids_at_y = count_voids(matrix)

    galaxies = [(x + voids_at_x[x]*extra, y + voids_at_y[y]*extra)
                for y in range(h) for x in range(w) if matrix[y][x] == '#']

    return sum(distance(a, b) for a, b in combinations(galaxies, 2))


def solve_1(matrix):
    return solve(matrix, 2)


def solve_2(matrix):
    return solve(matrix, 1_000_000)


if __name__ == '__main__':
    matrix = parse_input('input.txt')

    print(f'Task 1: {solve_1(matrix)}')
    print(f'Task 2: {solve_2(matrix)}')
