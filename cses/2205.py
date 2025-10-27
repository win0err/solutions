from typing import Iterator


def solve(n: int) -> Iterator[str]:
    repetitions_left = [2 ** (i + 1) // 2 for i in range(n)]
    nums_at_pos = [0 for _ in range(n)]

    for _ in range(2**n):
        current = 0

        for pos in range(n):
            current |= nums_at_pos[pos] << pos

            repetitions_left[pos] -= 1

            if repetitions_left[pos] == 0:
                repetitions_left[pos] = 2 ** (pos + 1)

                nums_at_pos[pos] = 0 if nums_at_pos[pos] else 1

        yield f'{current:0{n}b}'


if __name__ == '__main__':
    n = int(input())

    for s in solve(n):
        print(s)
