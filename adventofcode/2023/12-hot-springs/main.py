from functools import cache, lru_cache


def parse_input(filename, expand=1):
    springs = []

    with open(filename, 'r+') as f:
        for line in f:
            conditions, arrangements = line.split(' ')

            conditions = '?'.join([conditions] * expand)
            arrangements = tuple(int(n) for n in arrangements.split(',')) * expand

            springs.append((conditions, arrangements))

    return springs


@cache
def generate_sequences(conditions, arragements=()):
    total = len(conditions)
    l, *r = arragements

    gaps = len(r)
    reserved = gaps + sum(r)

    available_up_to = total - reserved - l

    sequences = []
    for left_gap in range(available_up_to + 1):
        seq = '.' * left_gap + '#' * l
        subtotal = total - len(seq)

        mask_len = len(seq) + len('.')
        if not matches(seq, conditions[:mask_len]):
            continue

        if len(r) > 0:
            for subseq in generate_sequences(conditions[mask_len:], tuple(r)):
                sequences.append(seq + '.' + subseq)
        else:
            sequences.append(seq + '.' * subtotal)

    sequences = [s for s in sequences if matches(s, conditions)]

    return sequences


@cache
def matches(sequence, mask):
    return all(s == m or m == '?' for s, m in zip(sequence, mask))


def solve_1(filename):
    springs = parse_input(filename, 1)

    return sum(len(generate_sequences(c, a)) for c, a in springs)


def solve_2(filename):
    pass


if __name__ == '__main__':
    filename = 'input.txt'

    print(f'Task 1: {solve_1(filename)}')
    print(f'Task 2: {solve_2(filename)}')
