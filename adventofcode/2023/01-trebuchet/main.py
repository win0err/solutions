digits_as_words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def parse_line(line, parse_words):
    parsed = []

    for i in range(len(line)):
        if line[i].isdigit():
            parsed.append(int(line[i]))

        elif parse_words:
            for word, digit in digits_as_words.items():
                if line[i:].startswith(word):
                    parsed.append(digit)
                    break

    return parsed


def parse_input(filename, parse_words=False):
    data = []

    with open(filename, 'r+') as f:
        for line in f:
            digits = parse_line(line, parse_words)
            data.append((digits[0], digits[-1]))

    return data


def solve(data):
    return sum(l * 10 + r for (l, r) in data)


if __name__ == '__main__':
    data1 = parse_input('input.txt', False)
    data2 = parse_input('input.txt', True)

    print(f'Task 1: {solve(data1)}')
    print(f'Task 2: {solve(data2)}')
