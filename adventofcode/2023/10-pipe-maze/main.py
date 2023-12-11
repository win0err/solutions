from collections import deque
from itertools import batched


class c(tuple):
    def __add__(self, other):
        return c(c1 + c2 for c1, c2 in zip(self, other))


START = 'S'
OUTER = 'O'
EMPTY = '.'

NEIGHBOURS = [c((0, 1)), c((0, -1)), c((1, 0)), c((-1, 0))]

DIRECTIONS = {
    '|': [c((0, 1)), c((0, -1))],
    '-': [c((1, 0)), c((-1, 0))],
    'L': [c((1, 0)), c((0, -1))],
    'J': [c((-1, 0)), c((0, -1))],
    '7': [c((-1, 0)), c((0, 1))],
    'F': [c((1, 0)), c((0, 1))],
}

EXPAND = {
    'S': (('.', 'S', '.'),
          ('S', 'S', 'S'),
          ('.', 'S', '.')),

    'O': (('O', 'O', 'O'),
          ('O', 'O', 'O'),
          ('O', 'O', 'O')),

    '.': (('.', '.', '.'),
          ('.', '.', '.'),
          ('.', '.', '.')),

    '|': (('.', '#', '.'),
          ('.', '#', '.'),
          ('.', '#', '.')),

    '-': (('.', '.', '.'),
          ('#', '#', '#'),
          ('.', '.', '.')),

    'L': (('.', '#', '.'),
          ('.', '#', '#'),
          ('.', '.', '.')),

    'J': (('.', '#', '.'),
          ('#', '#', '.'),
          ('.', '.', '.')),

    '7': (('.', '.', '.'),
          ('#', '#', '.'),
          ('.', '#', '.')),

    'F': (('.', '.', '.'),
          ('.', '#', '#'),
          ('.', '#', '.')),
}



def parse_input(filename):
    tiles = {}
    w, h = 0, 0

    with open(filename, 'r+') as f:
        lines = f.read().strip().splitlines()
        w, h = len(lines[0]), len(lines)

        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                tiles[c((x, y))] = ch

    return tiles, (w, h)


class Loop:
    def __init__(self, tiles):
        self._tiles = tiles

        loop = [self._first_tile, self._second_tile]
        start = loop[0]

        while start != (point := self._move(loop[-1], loop[-2])):
            loop.append(point)

        self.loop = loop

    @property
    def _first_tile(self):
        for coords, ch in self._tiles.items():
            if ch == START:
                return coords

    @property
    def _second_tile(self):
        start = self._first_tile

        for diff in NEIGHBOURS:
            point = start + diff

            # if can return to the start from the current point
            if start in [point + diff for diff in DIRECTIONS[self._tiles[point]]]:
                return point

    def _move(self, curr, prev):
        if self._tiles[curr] not in DIRECTIONS:
            return curr

        diff1, diff2 = DIRECTIONS[self._tiles[curr]]
        a, b = curr + diff1, curr + diff2

        return a if a != prev else b



class Grid:
    def __init__(self, dimensions, tiles, loop):
        self.dimensions = dimensions
        w, h = dimensions

        self._loop = loop

        self.grid = [[EMPTY for x in range(w)] for y in range(h)]
        for coords in loop.loop:
            x, y = coords
            self.grid[y][x] = tiles[coords]

        self._init_big_grid()

    def _init_big_grid(self):
        _, h = self.dimensions
        big_grid = [[] for y in range(h*3)]

        for y, line in enumerate(self.grid):
            for ch in line:
                big_tile = EXPAND[ch]

                for i, tile_part in enumerate(big_tile):
                    big_grid[y*3 + i].extend(tile_part)

        self._big_grid = big_grid

    def find_outside_region(self):
        w, h = self.dimensions
        width, height = range(w*3), range(h*3)

        # 1. Find outer points in big grid
        # (0, 0) is always outside point in dataset, use this point instead of perimeter
        initial = c((0, 0))
        stack = deque([initial])

        while len(stack) > 0:
            point = stack.pop()
            x, y = point

            if self._big_grid[y][x] != EMPTY:
                continue

            self._big_grid[y][x] = OUTER

            for diff in NEIGHBOURS:
                neighbour = point + diff
                nx, ny = neighbour

                if nx in width and ny in height:
                    stack.append(neighbour)

        # 2. Mark outer points in the small grid
        for y, lines in enumerate(batched(self._big_grid, n=3)):
            big_tiles = zip(*list(batched(line, n=3) for line in lines))

            for x, tile in enumerate(big_tiles):
                if tile == EXPAND['O']:
                    self.grid[y][x] = 'O'

    def print(self, big=False):
        grid = self._big_grid if big else self.grid

        for line in grid:
            print(''.join(line))



def solve_1(loop):
    return len(loop.loop) // 2


def solve_2(grid):
    grid.find_outside_region()
    w, h = grid.dimensions

    return sum(grid.grid[y][x] == EMPTY for x in range(w) for y in range(h))


if __name__ == '__main__':
    tiles, dimensions = parse_input('input.txt')

    loop = Loop(tiles)
    grid = Grid(dimensions, tiles, loop)

    print(f'Task 1: {solve_1(loop)}')
    print(f'Task 2: {solve_2(grid)}')
