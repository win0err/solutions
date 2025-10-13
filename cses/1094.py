def solve(n, numbers):
    moves = 0

    for i in range(1, n):
        if numbers[i] >= numbers[i-1]:
            continue

        moves += numbers[i-1] - numbers[i]
        numbers[i] = numbers[i-1]

    return moves


if __name__ == '__main__':
    n = int(input())
    numbers = [int(x) for x in input().split(' ')]

    print(solve(n, numbers))
