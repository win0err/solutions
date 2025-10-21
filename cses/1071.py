def solve(y: int, x: int) -> int:
    overflow = 0

    if y >= x:
        overflow = x if y % 2 == 0 else 2*y - x
    else:
        overflow = 2*x - y if x % 2 == 0 else y

    return max(x, y) ** 2 - overflow + 1


if __name__ == '__main__':
    for _ in range(int(input())):
        r, c = map(int, input().split())

        print(solve(r, c))
