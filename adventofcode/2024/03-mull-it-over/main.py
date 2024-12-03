import re

RE_MUL = re.compile(r'(?:mul\((\d+),(\d+)\))')
RE_ENABLED_CODE = re.compile(r'(?:^|do\(\))(.+?)(?=$|don\'t\(\))')

def parse_input(filename):
    return open(filename, 'r+').read().replace('\n', '')


def execute(code):
    return sum(int(match[1]) * int(match[2]) for match in RE_MUL.finditer(code))


if __name__ == '__main__':
    all_code = parse_input('input.txt')
    enabled_code = ''.join(match[1] for match in RE_ENABLED_CODE.finditer(all_code))

    print(f'Task 1: {execute(all_code)}')
    print(f'Task 2: {execute(enabled_code)}')
