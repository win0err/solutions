import sys
from typing import TextIO


def solve(reader: TextIO):
    longest = 0
    current = 0

    prev_char = None

    while True:
        char = reader.read(1)

        if not char:
            break

        if char == prev_char:
            current += 1
        else:
            longest = max(longest, current)

            current = 1
            prev_char = char


    return max(longest, current)


if __name__ == '__main__':
    print(solve(sys.stdin))
