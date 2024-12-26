from collections import Counter, defaultdict
from math import prod
from typing import Dict, Tuple


class coords(tuple):
    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __add__(self, other):
        return coords(c1 + c2 for c1, c2 in zip(self, other))

    def __mul__(self, n: int):
        return coords((self.x * n, self.y * n))

    def __mod__(self, other):
        return coords((self.x % other.x, self.y % other.y))


def parse_input(filename: str) -> Dict[coords, str]:
    robots = []
    size = coords((101, 103) if filename == 'input.txt' else (11, 7))

    with open(filename, 'r+') as file:
        for y, line in enumerate(file):
            line = line.strip()

            p_part, v_part = line.split(' ')

            p = coords(map(int, p_part[2:].split(',')))
            v = coords(map(int, v_part[2:].split(',')))

            robots.append((p, v))

    return robots, size


def tick(robots, size, n=1):
    return [((pos + vel * n) % size, vel) for pos, vel in robots]


def solve_1(robots, size):
    state = tick(robots, size, n=100)

    quadrants = [0 for k in range(4)]

    for robot, _ in state:
        if robot.x < size.x // 2 and robot.y < size.y // 2:
            quadrants[0] += 1
        elif robot.x > size.x // 2 and robot.y < size.y // 2:
            quadrants[1] += 1
        elif robot.x < size.x // 2 and robot.y > size.y // 2:
            quadrants[2] += 1
        elif robot.x > size.x // 2 and robot.y > size.y // 2:
            quadrants[3] += 1

    return prod(quadrants)


if __name__ == '__main__':
    robots, size = parse_input('input.txt')

    print(f'Task 1: {solve_1(robots, size)}')
    print(f'Task 2: {None}')
