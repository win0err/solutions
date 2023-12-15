from functools import reduce


def parse_input(filename):
    with open(filename, 'r+') as f:
        return f.readline().strip().split(',')


def hash(seq):
    return reduce(lambda v, ch: (v + ord(ch)) * 17 % 256, seq, 0)


def solve_1(sequences):
    return sum(hash(sequence) for sequence in sequences)


def solve_2(sequences):
    boxes = [{} for _ in range(256)]

    for sequence in sequences:
        if sequence.endswith('-'):
            name = sequence[:-1]
            boxes[hash(name)].pop(name, None)
        else:
            name, value = sequence.split('=')
            boxes[hash(name)][name] = int(value)

    power = 0
    for bid, box in enumerate(boxes, start=1):
        power += sum(bid * sid * focal for sid, focal
                     in enumerate(box.values(), start=1))

    return power


if __name__ == '__main__':
    sequences = parse_input('input.txt')

    print(f'Task 1: {solve_1(sequences)}')
    print(f'Task 2: {solve_2(sequences)}')
