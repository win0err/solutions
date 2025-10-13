def solve(n, numbers):
    def recursive(idx = 0, bucket1 = 0, bucket2 = 0):
        if idx == n:
            return abs(bucket1 - bucket2)

        return min(
            recursive(idx+1, numbers[idx] + bucket1, bucket2),
            recursive(idx+1, bucket1, numbers[idx] + bucket2),
        )

    return recursive()


if __name__ == '__main__':
    n = int(input())
    numbers = [int(x) for x in input().split(' ')]

    print(solve(n, numbers))
