from itertools import combinations, pairwise


def parse_input(filename):
    with open(filename, 'r+') as file:
        return list(tuple(int(n) for n in line.split()) for line in file)


def is_safe_report(report: list):
    is_increasing = all(a < b for a, b in pairwise(report))
    is_decreasing = all(a > b for a, b in pairwise(report))

    is_diff_ok = all(1 <= abs(a - b) <= 3 for a, b in pairwise(report))

    return (is_increasing or is_decreasing) and is_diff_ok


def are_report_variations_safe(report: list):
    return any(is_safe_report(variation) for variation
               in combinations(report, len(report) - 1))


if __name__ == '__main__':
    reports = parse_input('input.txt')

    safe_count = sum(int(is_safe_report(report)) for report in reports)
    safe_count_with_variations = sum(int(is_safe_report(report) or are_report_variations_safe(report)) for report in reports)

    print(f'Task 1: {safe_count}')
    print(f'Task 2: {safe_count_with_variations}')
