from itertools import combinations
from heapq import nlargest
from math import dist, prod


type Coord3 = tuple[int, int, int]


def get_sorted_pairs(coords: list[Coord3]) -> list[tuple[Coord3, Coord3]]:
    return sorted(combinations(coords, 2), key=lambda p: dist(*p))


def parse_input(filename: str) -> list[Coord3]:
    with open(filename) as file:
        lines = file.read().splitlines()

    result: list[Coord3] = []

    for line in lines:
        x, y, z = map(int, line.split(','))
        result.append((x, y, z))

    return result


def connect(coords: list[Coord3], sorted_pairs: list[tuple[Coord3, Coord3]], limit: int | None = None):
    # TODO: Union-Find algorithm

    circuits: list[set[Coord3]] = []
    lookup: dict[Coord3, set[Coord3]] = {}

    connected_boxes = set()
    last_pair = None

    for i, pair in enumerate(sorted_pairs):
        if limit is not None and i >= limit:
            break

        connected_boxes.update(pair)

        box1_circuit, box2_circuit = (lookup.get(b) for b in pair)

        if box1_circuit is None and box2_circuit is None:
            circuit = set(pair)
            circuits.append(circuit)

        elif box1_circuit is not None and box2_circuit is not None:
            if box1_circuit != box2_circuit:
                circuit = box1_circuit | box2_circuit

                circuits.remove(box1_circuit)
                circuits.remove(box2_circuit)
                circuits.append(circuit)

        else:
            circuit = box1_circuit or box2_circuit
            circuit.update(pair)

        for box in circuit:
            lookup[box] = circuit


        if len(coords) == len(connected_boxes) and len(circuits) == 1:
            last_pair = pair

            break

    return circuits, last_pair


def solve_1(coords: list[Coord3], sorted_pairs: list[tuple[Coord3, Coord3]]):
    circuits, _ = connect(coords, sorted_pairs, 1_000)

    return prod(nlargest(3, (len(c) for c in circuits)))


def solve_2(coords: list[Coord3], sorted_pairs: list[tuple[Coord3, Coord3]]):
    _, last_pair = connect(coords, sorted_pairs)

    if last_pair:
        box1, box2 = last_pair

        return box1[0] * box2[0]


if __name__ == '__main__':
    coords = parse_input('input.txt')
    pairs = get_sorted_pairs(coords)

    print(f'Task 1: {solve_1(coords, pairs)}')
    print(f'Task 2: {solve_2(coords, pairs)}')
