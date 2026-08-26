from itertools import combinations


type Coords = tuple[int, int]


def parse_input(filename: str) -> list[Coords]:
    with open(filename) as file:
        lines = file.read().splitlines()

    result: list[Coords] = []

    for line in lines:
        x, y = map(int, line.split(','))
        result.append((x, y))

    return result



def solve_1(coords: list[Coords]):
    return max(
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for (x1, y1), (x2, y2) in combinations(coords, 2)
    )



if __name__ == '__main__':
    coords = parse_input('input.txt')

    print(f'Task 1: {solve_1(coords)}')
    print(f'Task 2: {None}')
