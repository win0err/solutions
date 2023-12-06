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
            time = distance / speed + delay

            if time < record:
                options += 1

        result *= options

    return result


def solve_2(race):
    record, distance = race

    loses = 0
    for delay in range(1, distance):
        speed = delay
        time = distance / speed + delay

        if time >= record:
            loses += 1
        else:
            break

    return record - (loses * 2) - 1



if __name__ == '__main__':
    races = parse_input('input.txt', False)
    race = parse_input('input.txt', True)

    print(f'Task 1: {solve_1(races)}')
    print(f'Task 2: {solve_2(race)}')
