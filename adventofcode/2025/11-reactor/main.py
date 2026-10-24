def parse_input(filename: str) -> dict[str, list[str]]:
    with open(filename) as file:
        d = dict()

        for line in file:
            key, *values = line.strip().split(' ')

            d[key[:-1]] = values

    return d


START = 'you'
END = 'out'


def solve_1(g: dict[str, list[str]]) -> int:
    def dfs(key: str) -> int:
        if key == END:
            return 1

        return sum(dfs(child) for child in g.get(key, []))

    return dfs(START)


if __name__ == '__main__':
    graph = parse_input('input.txt')

    print(f'Task 1: {solve_1(graph)}')
    # print(f'Task 2: {solve_2(graph)}')
