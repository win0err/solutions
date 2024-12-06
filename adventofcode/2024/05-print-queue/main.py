from collections import defaultdict


def parse_input(filename):
    content = open(filename, 'r+').read().strip()

    raw_rules, raw_updates = content.split('\n\n')

    rules = defaultdict(set)
    reversed_rules = defaultdict(set)

    updates = []

    for r in raw_rules.split('\n'):
        first, second = map(int, r.split('|'))

        rules[first].add(second)
        reversed_rules[second].add(first)

    for u in raw_updates.split('\n'):
        updates.append(list(int(n) for n in u.split(',')))

    return (rules, reversed_rules), updates


def is_valid_update(update, rules):
    prev_pages = [*update]
    while prev_pages:
        should_not_be_prev = rules[prev_pages.pop()]

        if set.intersection(should_not_be_prev, set(prev_pages)):
            return False

    return True


def filter_updates(updates, rules):
    valid_updates = []
    invalid_updates = []

    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    return valid_updates, invalid_updates


def sum_middles(updates):
    return sum(update[len(update) // 2] for update in updates)


def topological_sort(graph):
    visited = {}
    result = []

    def dfs(node):
        if node in visited:
            return

        visited[node] = True

        for neighbor in graph.get(node, []):
            dfs(neighbor)

        result.append(node)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return result


def fix_update(update, reversed_rules):
    graph = { page: list(dest for dest in reversed_rules[page] if dest in update) for page in update}

    return topological_sort(graph)


if __name__ == '__main__':
    all_rules, updates = parse_input('input.txt')
    rules, reversed_rules = all_rules

    valid, invalid = filter_updates(updates, rules)
    fixed = [fix_update(update, reversed_rules) for update in invalid]

    print(f'Task 1: {sum_middles(valid)}')
    print(f'Task 2: {sum_middles(fixed)}')
