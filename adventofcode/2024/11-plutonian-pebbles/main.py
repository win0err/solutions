def parse_input(filename):
    return [int(n) for n in open(filename, 'r+').readline().strip().split()]


def blink(stones):
    new_stones = []

    for n in stones:
        s = str(n)
        l = len(s)

        if n == 0:
            new_stones.append(1)
        elif len(s) % 2 == 0:
            new_stones.append(int(s[:l//2]))
            new_stones.append(int(s[l//2:]))
        else:
            new_stones.append(n*2024)

    return new_stones


def count(stones, times):
    s = [*stones]

    for _ in range(times):
        s = blink(s)

    return len(s)


if __name__ == '__main__':
    stones = parse_input('input.txt')

    print(f'Task 1: {count(stones, 25)}')
    # print(f'Task 2: {count(stones, 75)}')
