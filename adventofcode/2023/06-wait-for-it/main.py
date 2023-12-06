import math


def parse_input(filename, fix_kerning=False):
    with open(filename, 'r+') as f:
        times, distances = f.read().strip().splitlines()

    times = times.split(':')[1].strip()
    distances = distances.split(':')[1].strip()

    if fix_kerning:
        times = times.replace(' ', '')
        distances = distances.replace(' ', '')

        return int(times), int(distances)

    times = [int(n) for n in times.split()]
    distances = [int(n) for n in distances.split()]

    return zip(times, distances)


def solve_1(races):
    result = 1

    for (record, distance) in races:
        options = 0

        for delay in range(1, distance):
            speed = delay

            # distance = speed * t
            t = distance / speed

            if t + delay < record:
                options += 1

        result *= options

    return result


def solve_2(race):
    t, d = race

    # speed = delay
    #
    # distance = speed * t
    # t = distance / speed (+ delay)
    # t - delay = distance / speed
    #
    # distance = speed * (t - delay)
    #
    # x = speed = delay
    #
    # distance = x * (t - x)
    # distance = x * t - x^2
    #
    # ax^2 + bx + c = 0
    # x1 = (-b + sqrt(b^2 - 4ac)) / 2a
    # x2 = (-b - sqrt(b^2 - 4ac)) / 2a
    #
    # x^2 - t * x + distance = 0
    # x1 = (t - sqrt(t^2 - 4 * distance) / 2
    # x2 = (t + sqrt(t^2 - 4 * distance) / 2

    # t = record (time when we start winning)

    x1 = (t - math.sqrt(t**2 - 4 * d)) // 2
    x2 = (t + math.sqrt(t**2 - 4 * d)) // 2

    return int(abs(x1 - x2))


if __name__ == '__main__':
    races = parse_input('input.txt', False)
    race = parse_input('input.txt', True)

    print(f'Task 1: {solve_1(races)}')
    print(f'Task 2: {solve_2(race)}')
