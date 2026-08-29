from itertools import combinations, pairwise

type Coords = tuple[int, int]
type Edge = tuple[Coords, Coords]


def parse_input(filename: str) -> list[Coords]:
    with open(filename) as file:
        lines = file.read().splitlines()

    result: list[Coords] = []

    for line in lines:
        x, y = map(int, line.split(','))
        result.append((x, y))

    return result


def has_intersection(e1: Edge, e2: Edge):
    (x11, y11), (x12, y12) = e1
    (x21, y21), (x22, y22) = e2

    x_overlap = min(x11, x12) < max(x21, x22) and min(x21, x22) < max(x11, x12)
    y_overlap = min(y11, y12) < max(y21, y22) and min(y21, y22) < max(y11, y12)

    return x_overlap and y_overlap


def solve_1(coords: list[Coords]):
    return max(
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for (x1, y1), (x2, y2) in combinations(coords, 2)
    )


def solve_2(coords: list[Coords]):
    # TODO: prepare and sort bounds
    edges: list[Edge] = list(pairwise(coords + coords[:1]))
    largest = 0

    for edge in combinations(coords, 2):
        if not any(has_intersection(edge, e) for e in edges):
            (x1, y1), (x2, y2) = edge
            largest = max(largest, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

    return largest


if __name__ == '__main__':
    coords = parse_input('input.txt')

    print(f'Task 1: {solve_1(coords)}')
    print(f'Task 2: {solve_2(coords)}')
