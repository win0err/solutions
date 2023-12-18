from itertools import pairwise


def parse_input(filename):
    # x - real, y - imag
    DIFFS = {'R': 1 + 0j, 'D': 0 + 1j, 'L': -1 + 0j, 'U': 0 - 1j}

    with open(filename, 'r+') as f:
        polygon_a = [0]
        polygon_b = [0]

        for line in f:
            direction, count, unparsed = line.split(' ')
            polygon_a.append(polygon_a[-1] + DIFFS[direction] * int(count))

            direction = "RDLU"[int(unparsed[-3])]
            count = int(unparsed[2:-3], base=16)
            polygon_b.append(polygon_b[-1] + DIFFS[direction] * int(count))

        return polygon_a, polygon_b


def solve(vertices):
    area = 0
    boundary_points = 0

    edges = pairwise(vertices)  # closed polygon

    for start, end in edges:
        # shoelace formula, https://mathworld.wolfram.com/PolygonArea.html
        area += (start.real * end.imag - end.real * start.imag) / 2
        boundary_points += abs(end - start)  # edge length

    # Pick's theorem, https://mathworld.wolfram.com/PicksTheorem.html
    # area = internal_points + boundary_points/2 - 1
    # internal_points = area - boundary_points/2 + 1

    # we need to return number of both internal and boundary _points_
    # internal_points + boundary_points =>
    #  area - boundary_points/2 + 1 + boundary_points =>
    #  area + boundary_points/2 + 1
    return int(area + boundary_points / 2 + 1)


if __name__ == '__main__':
    a, b = parse_input('input.txt')

    print(f'Task 1: {solve(a)}')
    print(f'Task 2: {solve(b)}')
