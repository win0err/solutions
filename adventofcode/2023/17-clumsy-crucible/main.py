from heapq import heappop, heappush
from math import inf


DOWN = (0, 1)
UP = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)

ALL_DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

SAME_DIRECTIONS = {UP: [UP], DOWN: [DOWN], LEFT: [LEFT], RIGHT: [RIGHT]}
TURN_DIRECTIONS = {UP: [LEFT, RIGHT], DOWN: [LEFT, RIGHT],
                   LEFT: [UP, DOWN], RIGHT: [UP, DOWN]}

def parse_input(filename):
    with open(filename, 'r+') as f:
        points = {(x, y): int(w)
                  for y, line in enumerate(f)
                  for x, w in enumerate(line.strip())}

        coords = sorted(list(points.keys()))
        start, end = coords[0], coords[-1]

        return dict(points), start, end


def search(matrix, start, end, min_run=1, max_run=inf):
    w, h = range(start[0], end[0] + 1), range(start[1], end[1] + 1)

    visited = set()
    pq = [(0, (start, None, 0))]

    while len(pq) > 0:
        distance, configuration = heappop(pq)
        point, _, run_len = configuration

        if point == end and run_len >= min_run:
            return distance

        neighbours = get_neighbours(configuration, w, h, min_run, max_run)
        for new_configuration in neighbours:
            if new_configuration not in visited:
                visited.add(new_configuration)

                nx, ny = new_configuration[0]
                neighbour_distance = distance + matrix[(nx, ny)]

                heappush(pq, (neighbour_distance, new_configuration))

    return -1


def get_neighbours(configuration, w, h, min_run, max_run):
    point, run_dir, run_len = configuration

    if run_len == 0:
        directions = ALL_DIRECTIONS
    elif run_len < min_run:
        directions = SAME_DIRECTIONS[run_dir]
    elif run_len < max_run:
        directions = SAME_DIRECTIONS[run_dir] + TURN_DIRECTIONS[run_dir]
    elif run_len == max_run:
        directions = TURN_DIRECTIONS[run_dir]

    x, y = point
    neighbours = []

    for direction in directions:
        dx, dy = direction
        neighbour = x + dx, y + dy
        nx, ny = neighbour

        next_run_len = 1
        if direction == run_dir:
            next_run_len += run_len

        if nx in w and ny in h:
            neighbours.append((neighbour, direction, next_run_len))

    return neighbours


def solve_1(points, start, end):
    return search(points, start, end, min_run=1, max_run=3)


def solve_2(points, start, end):
    return search(points, start, end, min_run=4, max_run=10)


if __name__ == '__main__':
    points, start, end = parse_input('input.txt')

    print(f'Task 1: {solve_1(points, start, end)}')
    print(f'Task 2: {solve_2(points, start, end)}')
