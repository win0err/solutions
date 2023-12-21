START = 'S'
PLOT = '.'
ROCK = '#'

STEPS_COUNT_1 = 64
STEPS_COUNT_2 = 26_501_365

LRUD = (-1, 1, -1j, 1j)


def parse_input(filename):
    with open(filename, 'r+') as f:
        garden = {}
        start = None

        for y, line in enumerate(f):
            for x, ch in enumerate(line.strip()):
                garden[complex(x, y)] = ch

                if ch == START:
                    start = complex(x, y)

        return garden, start


def walk(garden, start, steps, infinite=False):
    side = int(len(garden)**.5)  # garden is a square
    at = set([start])

    def normalize(point):
        return complex(point.real % side, point.imag % side)

    for _ in range(steps):
        to = set()

        for point in at:
            destinations = [point + d for d in LRUD]
            if not infinite:
                destinations = [dst for dst in destinations
                                if dst in garden]

            to.update(dst for dst in destinations
                      if garden[normalize(dst)] != ROCK)

        at = to

    return len(at)


def solve_1(garden, start):
    return walk(garden, start, STEPS_COUNT_1)


def solve_2(garden, start):
    side = int(len(garden)**.5)  # garden is a square

    x = STEPS_COUNT_2 // side
    n = STEPS_COUNT_2 % side

    b0 = walk(garden, start, n, infinite=True)
    b1 = walk(garden, start, n+side, infinite=True)
    b2 = walk(garden, start, n+side*2, infinite=True)

    # source: https://github.com/apprenticewiz/adventofcode/blob/main/2023/rust/day21b/src/main.rs#L85-L104

    det_a = -2.0
    det_a0 = -b0 + 2.0 * b1 - b2
    det_a1 = 3.0 * b0 - 4.0 * b1 + b2
    det_a2 = -2.0 * b0

    a = det_a0 / det_a
    b = det_a1 / det_a
    c = det_a2 / det_a

    return int(a * x**2 + b * x + c)


if __name__ == '__main__':
    garden, start = parse_input('input.txt')

    print(f'Task 1: {solve_1(garden, start)}')
    print(f'Task 2: {solve_2(garden, start)}')
