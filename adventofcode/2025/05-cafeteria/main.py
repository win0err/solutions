def merge_intervals(intervals: list[range]):
    merged: list[range] = []

    for r in sorted(intervals, key=lambda r: r.start):
        if merged and r.start <= merged[-1].stop:
            merged[-1] = range(merged[-1].start, max(merged[-1].stop, r.stop))
        else:
            merged.append(r)

    return merged


def parse_range(s: str) -> range:
    start, end = map(int, s.split('-'))

    return range(start, end + 1)


def parse_input(filename: str) -> tuple[list[range], list[int]]:
    with open(filename) as file:
        intervals, values = (part.splitlines() for part in file.read().split('\n\n'))

        intervals = merge_intervals([parse_range(i) for i in intervals])
        values = [int(i) for i in values]

        return intervals, values


def solve_1(intervals: list[range], values: list[int]):
    return sum(any(ingredient in r for r in intervals)
               for ingredient in values)


def solve_2(intervals: list[range]):
    return sum(len(i) for i in intervals)


if __name__ == '__main__':
    intervals, values = parse_input('input.txt')

    print(f'Task 1: {solve_1(intervals, values)}')
    print(f'Task 2: {solve_2(intervals)}')
