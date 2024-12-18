from collections import Counter


def parse_input(filename):
    return [int(n) for n in open(filename, 'r+').readline().strip().split()]


def blink(prev_state: Counter):
    state = Counter(prev_state)

    for stone, amount in prev_state.items():
        s = str(stone)
        mid = len(s) // 2

        if stone == 0:
            state[0] -= amount
            state[1] += amount

        elif len(s) % 2 == 0:
            state[stone] -= amount

            state[int(s[:mid])] += amount
            state[int(s[mid:])] += amount

        else:
            state[stone] -= amount
            state[stone*2024] += amount

    return state


def count(stones, times):
    state = Counter(stones)

    for _ in range(times):
        state = blink(state)

    return sum(state.values())


if __name__ == '__main__':
    stones = parse_input('input.txt')

    print(f'Task 1: {count(stones, 25)}')
    print(f'Task 2: {count(stones, 75)}')
