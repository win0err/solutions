from enum import Enum
from math import prod
from operator import gt, lt
from queue import deque
import re


Instruction = Enum('Instruction', ['JMP', 'CMP', 'RET'])

class Operator(Enum):
    GT = '>'
    LT = '<'

    def compare(self, a, b):
        return {Operator.GT: gt, Operator.LT: lt}[self](a, b)


def parse_input(filename):
    workflows = {}
    ratings = []

    with open(filename, 'r+') as f:
        raw_workflows, raw_ratings = map(lambda lines: lines.splitlines(),
                                         f.read().strip().split('\n\n'))

        for raw in raw_workflows:
            name, raw_instructions = raw.strip()[:-1].split('{')
            raw_instructions = re.split(r'[:,]', raw_instructions)

            workflow = []

            for code in raw_instructions:
                if '<' in code or '>' in code:
                    var, op, val = code[0], code[1], code[2:]
                    payload = Operator(op), var, int(val)

                    workflow.append((Instruction.CMP, payload))
                elif code in 'AR':
                    workflow.append((Instruction.RET, code == 'A'))
                else:
                    workflow.append((Instruction.JMP, code))

            workflows[name] = workflow

        for raw in raw_ratings:
            raw = raw.strip()[1:-1]
            rating = {}

            for expression in raw.split(','):
                var, val = expression.split('=')
                rating[var] = int(val)

            ratings.append(rating)

    return workflows, ratings


def run(workflows, rating, start_workflow='in'):
    workflow = workflows[start_workflow]

    while True:
        rules = iter(workflow)

        for instr, payload in rules:
            match instr:
                case Instruction.CMP:
                    op, var, val = payload
                    truthy = op.compare(rating[var], val)

                    if not truthy:
                        next(rules)  # skip truthy branch

                case Instruction.JMP:
                    workflow = workflows[payload]
                    break

                case Instruction.RET:
                    return payload


def solve_1(workflows, ratings):
    return sum(sum(rating.values()) for rating in ratings
               if run(workflows, rating))


def solve_2(workflows):
    combinations = 0

    queue = deque([
        ('in', {ch: range(1, 4_001) for ch in 'xmas'})
    ])

    while queue:
        key, state = queue.popleft()
        if isinstance(key, bool):
            combinations += prod(len(r) for r in state.values()) if key else 0
            continue

        workflow = iter(workflows[key])
        for instr, payload in workflow:
            match instr:
                case Instruction.JMP | Instruction.RET:
                    queue.append((payload, state))

                case Instruction.CMP:
                    op, ch, mid = payload
                    l, r = state[ch].start, state[ch].stop

                    match op:
                        case Operator.LT:
                            truthy, falsy = range(l, mid), range(mid, r)
                        case Operator.GT:
                            falsy, truthy = range(l, mid + 1), range(mid + 1, r)

                    truthy_state = state | {ch: truthy}
                    falsy_state = state | {ch: falsy}

                    _, dest = next(workflow)  # truthy branch
                    queue.append((dest, truthy_state))

                    # keep processing falsy branch
                    state = falsy_state

    return combinations


if __name__ == '__main__':
    workflows, ratings = parse_input('input.txt')

    print(f'Task 1: {solve_1(workflows, ratings)}')
    print(f'Task 2: {solve_2(workflows)}')
