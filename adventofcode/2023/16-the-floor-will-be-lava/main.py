from queue import deque


class coords(tuple):
    def __add__(self, other):
        return coords(c1 + c2 for c1, c2 in zip(self, other))


UP = coords((0, -1))
DOWN = coords((0, 1))
RIGHT = coords((1, 0))
LEFT = coords((-1, 0))


# from → direction → to mapping
MOVES = {
    '.': {UP: [UP], DOWN: [DOWN], RIGHT: [RIGHT], LEFT: [LEFT]},
    '/': {UP: [RIGHT], DOWN: [LEFT], RIGHT: [UP], LEFT: [DOWN]},
    '\\': {UP: [LEFT], DOWN: [RIGHT], RIGHT: [DOWN], LEFT: [UP]},
    '|': {UP: [UP], DOWN: [DOWN], RIGHT: [UP, DOWN], LEFT: [UP, DOWN]},
    '-': {UP: [LEFT, RIGHT], DOWN: [LEFT, RIGHT], RIGHT: [RIGHT], LEFT: [LEFT]},
}


def parse_input(filename):
    with open(filename, 'r+') as f:
        layout = {}

        for y, row in enumerate(f):
            for x, tile in enumerate(row.strip()):
                layout[coords((x, y))] = tile

        w, h = list(layout.keys())[-1]

        return layout, (w + 1, h + 1)


def get_energized_points(layout, start, direction):
    visited = set()

    queue = deque([(start, direction)])
    while len(queue) > 0:
        state = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        point, direction = state
        tile = layout[point]

        queue.extend((point + to, to) for to in MOVES[tile][direction]
                     if point + to in layout)

    return len(set(c for c, _ in visited))


def solve_1(layout):
    start = coords((0, 0))
    return get_energized_points(layout, start, RIGHT)


def solve_2(layout, dimensions):
    w, h = dimensions

    configurations = []
    for x in range(w):
        configurations.extend([
            (coords((x, 0)), DOWN),
            (coords((x, h-1)), UP),
        ])

    for y in range(h):
        configurations.extend([
            (coords((0, y)), RIGHT),
            (coords((w-1, y)), LEFT),
        ])

    return max(get_energized_points(layout, start, direction)
               for start, direction in configurations)


if __name__ == '__main__':
    layout, dimensions = parse_input('input.txt')

    print(f'Task 1: {solve_1(layout)}')
    print(f'Task 2: {solve_2(layout, dimensions)}')
