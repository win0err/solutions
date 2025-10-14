from collections import Counter


def solve(line: str):
    symbols = Counter(line)

    result = ''
    single_char = ''

    for ch, cnt in symbols.items():
        result += ch * (cnt // 2)

        if cnt % 2 != 0:
            if single_char:
                return 'NO SOLUTION'

            single_char = ch

    return result + single_char + result[::-1]


if __name__ == '__main__':
    print(solve(input()))
