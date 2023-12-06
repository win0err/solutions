def parse_input(filename):
    seeds = []
    maps = []

    with open(filename, 'r+') as f:
        seeds, *raw_maps = f.read().strip().split('\n\n')

    seeds = seeds.split(':')[1]
    seeds = [int(n) for n in seeds.split()]

    for m in raw_maps:
        _, *m = m.splitlines()
        instructions = []

        for instruction in m:
            dst, src, n = [int(n) for n in instruction.split()]
            instructions.append(
                (range(src, src + n), dst - src)
            )

        maps.append(instructions)

    return seeds, maps


def _translate_location(n, instructions):
    for src_range, delta in instructions:
        if n in src_range:
            return n + delta

    return n


def _seeds_to_ranges(seeds):
    seed_ranges = []

    for i in range(0, len(seeds), 2):
        seed_ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))

    return seed_ranges


def solve_1(seeds, maps):
    locations = []

    for seed in seeds:
        loc = seed

        for instructions in maps:
            loc = _translate_location(loc, instructions)

        locations.append(loc)

    return min(locations)


def solve_2(seeds, maps):
    seeds = _seeds_to_ranges(seeds)

    for m in maps:
        processed_seeds = []

        for s in seeds:
            # only if seed range has intersection with instruction range
            intersections = [(r, delta) for (r, delta) in m
                             if s.stop > r.start and r.stop > s.start]

            if not intersections:
                processed_seeds.append(s)
                continue

            for r, delta in intersections:
                # seed => [ls) + [mid) + [rs)
                mid = range(max(s.start, r.start), min(s.stop, r.stop))
                ls = range(s.start, mid.start)
                rs = range(mid.stop, s.stop)

                if ls:
                    seeds.append(ls)

                if rs:
                    seeds.append(rs)

                processed_seeds.append(range(mid.start + delta, mid.stop + delta))

        seeds = processed_seeds

    return min(s.start for s in seeds)


if __name__ == '__main__':
    seeds, maps = parse_input('input.txt')

    print(f'Task 1: {solve_1(seeds, maps)}')
    print(f'Task 2: {solve_2(seeds, maps)}')
