from collections import deque
from dataclasses import dataclass
import re


pattern = re.compile(r"\[([^\]]+)\]\s+(.+?)\s+\{([^}]+)\}")
subpattern = re.compile(r"\(([^\)]+)\)")


@dataclass
class Machine:
    target_state: tuple[bool, ...]
    target_joltage: tuple[int, ...]
    vectors: list[tuple[int, ...]]

    @classmethod
    def from_string(cls, line: str):
        m = pattern.match(line)
        assert m is not None

        left, mid, right = m.groups()
        l = len(left)

        return cls(
            tuple(ch == '#' for ch in left),
            tuple(int(x) for x in right.split(",")),
            [cls.button_to_vector(button, l)
             for button in subpattern.findall(mid)],
        )


    @staticmethod
    def button_to_vector(button: str, l: int):
        indexes = [int(i) for i in button.split(",")]

        return tuple(1 if i in indexes else 0 for i in range(l))


def parse_input(filename: str) -> list[Machine]:
    with open(filename) as file:
        lines = file.read().splitlines()

    return [Machine.from_string(line) for line in lines]


def bfs_states(m: Machine):
    start = tuple(False for _ in m.target_state)

    queue = deque([start])
    visited = {start}

    distances  = {start: 0}

    while state := queue.popleft():
        if state == m.target_state:
            return distances[state]

        for vector in m.vectors:
            next_state = tuple(not v if vector[i] else v for i, v in enumerate(state))

            if next_state not in visited:
                distances[next_state] = distances[state] + 1

                visited.add(next_state)
                queue.append(next_state)

    return 0


def bfs_joltages(m):
    start = tuple(m.target_joltage)
    goal = tuple(0 for _ in m.target_joltage)

    queue = deque([start])
    visited = {start}
    dist = {start: 0}

    vectors = sorted(m.vectors, reverse=True)

    while queue:
        state = queue.popleft()

        if state == goal:
            return dist[state]

        for vector in vectors:
            next_state = tuple(state[i] - vector[i] for i in range(len(state)))

            if any(next_state[i] < 0 for i in range(len(state))):
                continue

            if next_state not in visited:
                visited.add(next_state)
                dist[next_state] = dist[state] + 1
                queue.append(next_state)

    return 0


def solve_1(machines: list[Machine]):
    return sum(bfs_states(m) for m in machines)


def solve_2(machines: list[Machine]):
    return sum(bfs_joltages(m) for m in machines)


if __name__ == '__main__':
    machines = parse_input('input.txt')

    print(f'Task 1: {solve_1(machines)}')
    # print(f'Task 2: {solve_2(machines)}')
