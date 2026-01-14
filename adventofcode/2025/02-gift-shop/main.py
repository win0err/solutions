from itertools import batched


def parse_input(filename):
    with open(filename) as file:
        return [range(int(s), int(e)+1) for s, e in
                (r.split('-') for r in file.readline().strip().split(','))]


def solve_1(ranges: list[range]):
    count = 0

    for r in ranges:
        for n in r:
            s = str(n)

            if s[:len(s) // 2] == s[len(s) // 2:]:
                count += n

    return count


def solve_2(ranges: list[range]):
    answer = 0

    for r in ranges:
        for n in r:
            s = str(n)
            l = len(s)

            for batch in range(1, l // 2 + 1):
                if l % batch != 0:
                    continue

                if len(set(batched(s, batch))) == 1:
                    answer += n

                    break

    return answer


if __name__ == '__main__':
    ranges = parse_input('input.txt')

    print(f'Task 1: {solve_1(ranges)}')
    print(f'Task 2: {solve_2(ranges)}')
