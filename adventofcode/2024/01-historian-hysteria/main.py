from collections import Counter


def parse_input(filename):
    with open(filename, 'r+') as file:
        parsed = [(int(n) for n in line.split()) for line in file]

    return (sorted(l) for l in zip(*parsed))


if __name__ == '__main__':
    left, right = parse_input('input.txt')
    appearances = Counter(right)

    total_distance = 0
    similarity_score = 0

    for l, r in zip(left, right):
        total_distance = total_distance + abs(l - r)
        similarity_score = similarity_score + l * appearances.get(l, 0)

    print(f'Task 1: {total_distance}')
    print(f'Task 2: {similarity_score}')
