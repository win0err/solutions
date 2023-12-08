from itertools import cycle
from math import lcm


LEFT = 0
RIGHT = 1


def parse_input(filename):
    instructions = ''
    nodes = {}

    with open(filename, 'r+') as f:
        instructions, raw_nodes = f.read().strip().split('\n\n')
        instructions = [{'L': LEFT, 'R': RIGHT}[d] for d in instructions]

        for raw_node in raw_nodes.splitlines():
            node, l, r = raw_node[:3], raw_node[7:10], raw_node[12:15]
            nodes[node] = (l, r)

    return instructions, nodes


def move(start_node, instructions, nodes):
    node = start_node

    for instr in cycle(instructions):
        yield node
        node = nodes[node][instr]


def solve_1(instructions, nodes):
    for step, node in enumerate(move('AAA', instructions, nodes)):
        if node == 'ZZZ':
            return step


def solve_2(instructions, nodes):
    steps_to_finish = []

    for start_node in [n for n in nodes.keys() if n.endswith('A')]:
        for step, node in enumerate(move(start_node, instructions, nodes)):
            if node.endswith('Z'):
                steps_to_finish.append(step)
                break

    return lcm(*steps_to_finish)


if __name__ == '__main__':
    instructions, nodes = parse_input('input.txt')

    print(f'Task 1: {solve_1(instructions, nodes)}')
    print(f'Task 2: {solve_2(instructions, nodes)}')
