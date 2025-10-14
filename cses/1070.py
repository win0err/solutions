SEPARATOR = ' '


def solve(n: int):
    if n == 1:
        return '1'

    if n <= 3:
        return 'NO SOLUTION'

    odds = SEPARATOR.join(str(i)  for i in range(1, n + 1, 2))
    evens = SEPARATOR.join(str(i) for i in range(2, n + 1, 2))

    return evens + SEPARATOR + odds


if __name__ == '__main__':
    n = int(input())

    print(solve(n))
