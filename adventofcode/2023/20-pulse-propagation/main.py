from collections import defaultdict
from math import prod
from queue import deque


BUTTON = 'button'
BROADCASTER = 'broadcaster'
FLIP_FLOP = '%'
CONJUCTION = '&'

FINAL = 'rx'

HIGH = True
LOW = False


def parse_input(filename):
    with open(filename, 'r+') as f:
        configurations = {}

        for line in f:
            name, destinations = line.strip().split(' -> ')
            destinations = destinations.strip().split(', ')

            if name == BROADCASTER:
                module = name
            else:
                module = name[0]
                name = name[1:]

            configurations[name] = (module, destinations)

        return configurations


def create_state(configurations):
    ff_state = defaultdict(bool)
    conj_state = defaultdict(dict)

    for name, (module, destinations) in configurations.items():
        for dest in destinations:
            module = configurations.get(dest, None)

            if module and module[0] == CONJUCTION:
                conj_state[dest][name] = LOW

    return ff_state, conj_state


def step(configurations, state, task):
    ff_state, conj_state = state
    module, src, pulse = task

    if module not in configurations:
        return [], None

    module_type, destinations = configurations[module]

    if module_type == FLIP_FLOP:
        if pulse == HIGH:
            return [], None

        ff_state[module] = not ff_state[module]
        pulse = ff_state[module]

    if module_type == CONJUCTION:
        conj_state[module][src] = pulse
        pulse = not all(conj_state[module].values())

    return [(dest, module, pulse) for dest in destinations], pulse


def solve_1(configurations):
    count = {LOW: 0, HIGH: 0}
    state = create_state(configurations)

    for _ in range(1_000):
        q = deque([(BROADCASTER, BUTTON, LOW)])

        while q:
            task = q.popleft()

            _, _, pulse = task
            count[pulse] += 1

            next_tasks, _ = step(configurations, state, task)
            q.extend(next_tasks)

    return count[HIGH] * count[LOW]


def solve_2(configurations):
    inputs = defaultdict(list)
    for name, (module, destinations) in configurations.items():
        for dest in destinations:
            inputs[dest].append(name)

    # final module exists
    assert inputs.get(FINAL, None) is not None

    # final module have only 1 input
    assert len(inputs[FINAL]) == 1

    pre_final = inputs[FINAL][0]

    # type of the module that leads to the final module is conjuction
    assert configurations[pre_final][0] == CONJUCTION

    # all of it's inputs are conjuction modules too
    assert all(configurations[i][0] == CONJUCTION
               for i in inputs[pre_final])

    # we need to sent high pulse from each module
    # then pre final module will send a low pulse to the final
    sent_high_at = {m: 0 for m in inputs[pre_final]}

    state = create_state(configurations)

    press_count = 0
    while not all(sent_high_at.values()):
        q = deque([(BROADCASTER, BUTTON, LOW)])
        press_count += 1

        while q:
            task = q.popleft()
            module, _, _ = task

            next_tasks, sent_pulse = step(configurations, state, task)
            q.extend(next_tasks)

            if module in sent_high_at and sent_pulse == HIGH:
                sent_high_at[module] = press_count

    return prod(sent_high_at.values())


if __name__ == '__main__':
    configurations = parse_input('input.txt')

    print(f'Task 1: {solve_1(configurations)}')
    print(f'Task 2: {solve_2(configurations)}')
