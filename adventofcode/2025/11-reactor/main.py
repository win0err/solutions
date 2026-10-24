from functools import cache


def parse_input(filename: str) -> dict[str, list[str]]:
    with open(filename) as file:
        d = dict()

        for line in file:
            key, *values = line.strip().split(' ')

            d[key[:-1]] = values

    return d


def solve_1(g: dict[str, list[str]]) -> int:
    @cache
    def dfs(cur: str, end: str) -> int:
        return 1 if cur == end else sum(dfs(child, end) for child in g.get(cur, []))

    return dfs('you', 'out')


def solve_2(g: dict[str, list[str]]) -> int:
    @cache
    def dfs(cur: str, end: str, targets: tuple[str], reached = 0) -> int:
        if cur == end:
            return 1 if reached == len(targets) else 0

        return sum(dfs(child, end, targets, reached=reached+int(cur in targets))
                   for child in g.get(cur, []))

    return dfs('svr', 'out', ('fft', 'dac'))


if __name__ == '__main__':
    graph = parse_input('input.txt')

    print(f'Task 1: {solve_1(graph)}')
    print(f'Task 2: {solve_2(graph)}')
