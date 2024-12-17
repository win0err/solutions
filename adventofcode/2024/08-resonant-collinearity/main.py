from collections import defaultdict
from itertools import combinations

class coords(tuple):
    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __add__(self, other):
        return coords(c1 + c2 for c1, c2 in zip(self, other))

    def __sub__(self, other):
        return coords(c1 - c2 for c1, c2 in zip(self, other))

    def within_bounds(self, map_size):
        return 0 <= self.x <= size and 0 <= self.y <= size


def parse_input(filename):
    map = defaultdict(set)
    size = 0

    with open(filename, 'r+') as file:
        for y, line in enumerate(file):
            line = line.strip()
            size = y

            for x, char in enumerate(line):
                if char != '.':
                    map[char].add(coords((x, y)))

    return map, size


def get_antinodes(antennas, size, should_limit):
    antinodes = set()

    if not should_limit:
        antinodes.update(antennas)

    for first, second in combinations(antennas, 2):
        diff = second - first

        point = first - diff
        if point.within_bounds(size):
            antinodes.add(point)

        while not should_limit and point.within_bounds(size):
            antinodes.add(point)
            point -= diff


        point = second + diff
        if point.within_bounds(size):
            antinodes.add(point)

        while not should_limit and point.within_bounds(size):
            antinodes.add(point)
            point += diff

    return antinodes


def count_locations(antennas, size, should_limit):
    locations = set()

    for freq in map:
        locations.update(get_antinodes(map[freq], size, should_limit))

    return len(locations)


if __name__ == '__main__':
    map, size = parse_input('input.txt')

    print(f'Task 1: {count_locations(map, size, should_limit=True)}')
    print(f'Task 2: {count_locations(map, size, should_limit=False)}')
