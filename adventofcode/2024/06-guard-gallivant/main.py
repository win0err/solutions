from collections import defaultdict

START = '^'
OBSTRUCTION = '#'
EMPTY = '.'


class coords(tuple):
    def __add__(self, other):
        return coords(c1 + c2 for c1, c2 in zip(self, other))


class Directions:
    UP = coords((0, -1))
    DOWN = coords((0, 1))
    LEFT = coords((-1, 0))
    RIGHT = coords((1, 0))


def turn_right(direction):
    if direction == Directions.UP:
        return Directions.RIGHT
    elif direction == Directions.RIGHT:
        return Directions.DOWN
    elif direction == Directions.DOWN:
        return Directions.LEFT
    elif direction == Directions.LEFT:
        return Directions.UP

    raise Error('Unknown direction')


def parse_input(filename):
    start = None
    map = {}

    with open(filename, 'r+') as file:
        for y, line in enumerate(file):
            line = line.strip()

            for x, char in enumerate(line):
                point = coords((x, y))

                if char == START:
                    start = point

                map[point] = char

    return map, start


def simulate(map, point):
    direction = Directions.UP
    visited = defaultdict(set)

    while map.get(point, None) != None:
        if direction in visited[point]:
            return None  # cycle

        visited[point].add(direction)

        if map.get(point + direction, None) == OBSTRUCTION:
            direction = turn_right(direction)
        else:
            point += direction

    return list(visited.keys())


def solve_1(map, start):
    return len(simulate(map, start))


def solve_2(map, start):
    visited = simulate(map, start)
    count = 0

    for point in visited:
        if map.get(point) == EMPTY:
            map[point] = OBSTRUCTION

            if simulate(map, start) is None:
                count += 1

            map[point] = EMPTY

    return count


if __name__ == '__main__':
    map, start = parse_input('input.txt')

    print(f'Task 1: {solve_1(map, start)}')
    print(f'Task 2: {solve_2(map, start)}')
