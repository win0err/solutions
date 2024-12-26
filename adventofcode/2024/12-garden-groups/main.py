from collections import deque
from typing import Dict, Tuple
from itertools import product


class coords(tuple):
    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __add__(self, other):
        return coords(c1 + c2 for c1, c2 in zip(self, other))


DIRECTIONS = [
    coords((0, 1)),
    coords((1, 0)),
    coords((0, -1)),
    coords((-1, 0)),
]


def parse_input(filename: str) -> Dict[coords, str]:
    map = {}
    size = 0

    with open(filename, 'r+') as file:
        for y, line in enumerate(file):
            line = line.strip()
            size = y

            for x, char in enumerate(line):
                map[coords((x, y))] = char

    return map, size


def count_corners(map: Dict[coords, str], map_size: int, point: coords) -> int:
    region = map[point]

    num_corners = 0

    for dx, dy in product([1, -1], repeat=2):
        horizontal_neighbour = map.get(coords((point.x + dx, point.y)))
        vertical_neighbour = map.get(coords((point.x, point.y + dy)))
        diagonal_neighbour = map.get(coords((point.x + dx, point.y + dy)))

        # exterior corners
        if horizontal_neighbour != region and vertical_neighbour != region:
            num_corners += 1

        # interior corners
        if (
            horizontal_neighbour == region and vertical_neighbour == region
            and diagonal_neighbour != region
        ):
            num_corners += 1

    return num_corners


def solve(map: Dict[coords, str], map_size: int) -> Tuple[int, int]:
    visited = set()

    def bfs(start: coords):
        queue = deque([start])

        square = 0
        perimeter = 0
        sides = 0

        while queue:
            current = queue.popleft()
            if current in visited:
                continue

            visited.add(current)

            neighbours = [current + diff for diff in DIRECTIONS]
            same_neighbours = [n for n in neighbours if map.get(point) == map.get(n)]
            different_neighbours = [n for n in neighbours if map.get(point) != map.get(n)]

            square += 1
            sides += count_corners(map, map_size, current)
            perimeter += len(different_neighbours)

            queue.extend(same_neighbours)


        return square, perimeter, sides

    price = 0
    new_price = 0

    for point in map.keys():
        if point in visited:
            continue

        square, perimeter, sides = bfs(point)

        price += square * perimeter
        new_price += square * sides

    return price, new_price


if __name__ == '__main__':
    map, size = parse_input('input.txt')

    price, new_price = solve(map, size)

    print(f'Task 1: {price}')
    print(f'Task 2: {new_price}')
