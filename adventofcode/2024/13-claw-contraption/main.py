def parse_equations(input_string):
    lines = input_string.strip().split('\n')

    a1, b1, c1 = 0, 0, 0
    a2, b2, c2 = 0, 0, 0

    for line in lines:
        if line.startswith("Button A:"):
            parts = line.split(': ')[1].split(', ')

            a1 = int(parts[0].split('+')[1])
            a2 = int(parts[1].split('+')[1])

        elif line.startswith("Button B:"):
            parts = line.split(': ')[1].split(', ')

            b1 = int(parts[0].split('+')[1])
            b2 = int(parts[1].split('+')[1])

        elif line.startswith("Prize:"):
            parts = line.split(': ')[1].split(', ')

            c1 = int(parts[0].split('=')[1])
            c2 = int(parts[1].split('=')[1])

    return (a1, b1, c1), (a2, b2, c2)


def parse_input(filename):
    return [parse_equations(raw) for raw in open(filename, 'r+').read().strip().split('\n\n')]


def solve_system_of_equations(equations, should_multiply=False):
    a1, b1, c1 = equations[0]
    a2, b2, c2 = equations[1]

    if should_multiply:
        c1 += 10_000_000_000_000
        c2 += 10_000_000_000_000

    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    x = Dx / D
    y = Dy / D

    if x.is_integer() and y.is_integer():
        return int(x), int(y)

    return 0, 0


def solve(equations_list, should_multiply):
    return sum(x*3 + y for x, y in (solve_system_of_equations(equations, should_multiply)
                                    for equations in equations_list))


if __name__ == '__main__':
    equations_list = parse_input('input.txt')

    print(f'Task 1: {solve(equations_list, should_multiply=False)}')
    print(f'Task 2: {solve(equations_list, should_multiply=True)}')
