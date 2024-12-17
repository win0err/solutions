from math import inf


class coords(tuple):
    def __add__(self, other):
        return coords(c1 + c2 for c1, c2 in zip(self, other))


DIRECTIONS = [
    coords((0, -1)),
    coords((0, 1)),
    coords((-1, 0)),
    coords((1, 0)),
]

START = 0
END = 9


def parse_input(filename):
    map = {}

    with open(filename, 'r+') as file:
        for y, line in enumerate(file):
            line = line.strip()

            for x, char in enumerate(line):
                map[coords((x, y))] = int(char)

    return map


def get_score(map, distinct=True):
    def dfs(point, visited):
        if point in visited:
            return 0

        if distinct:
            visited.append(point)

        current_height = map.get(point)

        if current_height == END:
            return 1

        neighbours = [point + direction for direction in DIRECTIONS]
        valid_destinations = [n for n in neighbours if map.get(n, inf) - 1 == current_height]

        return sum(dfs(dest, visited) for dest in valid_destinations)

    return sum(dfs(point, visited=[]) for point in map if map[point] == START)


if __name__ == '__main__':
    map = parse_input('input.txt')

    print(f'Task 1: {get_score(map, distinct=True)}')
    print(f'Task 2: {get_score(map, distinct=False)}')
