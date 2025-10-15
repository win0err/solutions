from typing import Tuple


def solve(piles: Tuple[int, int]):
    min, max = sorted(piles)

    return (min + max) % 3 == 0 and min * 2 >= max


if __name__ == '__main__':
    for _ in range(int(input())):
        piles = tuple(map(int, input().split()))

        print('YES' if solve(piles) else 'NO')
