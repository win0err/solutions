def solve(numbers, bucket1=[], bucket2=[]):
    if not numbers:
        return abs(sum(bucket1) - sum(bucket2))

    n, *rest = numbers

    return min(
        solve(rest, [n] + bucket1, bucket2),
        solve(rest, bucket1, [n] + bucket2),
    )


if __name__ == '__main__':
    _ = input()
    numbers = [int(x) for x in input().split(' ')]

    print(solve(numbers))
