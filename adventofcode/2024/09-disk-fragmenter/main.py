from dataclasses import dataclass
from enum import Enum
from math import inf

@dataclass
class EmptySpace:
    length: int

    def __str__(self):
        return '.' * self.length


@dataclass
class File:
    id: int
    length: int

    def __str__(self):
        return str(self.id) * self.length


def parse_input(filename):
    equations = []

    numbers = [int(n) for n in open(filename, 'r+').readline().strip()]

    data = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
    free_space = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

    if len(free_space) < len(data):
        free_space.append(0)


    disk_map = []
    id = 0

    for i, length in enumerate(numbers):
        if i % 2 == 0:
            if length > 0:
                disk_map.append(File(id, length))

            id += 1
        else:
            if length > 0:
                disk_map.append(EmptySpace(length))

    return data, free_space, disk_map


def seq_sum(n, start=0):
    # n * (a + b) // 2
    return n * (start + (start + n - 1)) // 2


def solve_1(data_lengths, space_lengths):
    checksum = 0

    left_block_id = 0
    right_block_id = len(data_lengths) - 1
    space_id = 0

    i = 0

    while space_id < right_block_id:
        checksum += seq_sum(data_lengths[left_block_id], start=i) * left_block_id

        i += data_lengths[left_block_id]
        left_block_id += 1

        while space_lengths[space_id] > 0:
            if data[right_block_id] == 0:
                right_block_id -= 1

                continue

            number_of_blocks = min(space_lengths[space_id], data_lengths[right_block_id])

            checksum += seq_sum(number_of_blocks, start=i) * right_block_id

            i += number_of_blocks
            space_lengths[space_id] -= number_of_blocks
            data_lengths[right_block_id] -= number_of_blocks

        space_id += 1

    return checksum


def move_file(disk_map, src, dst):
    file: File = disk_map[src]
    space: EmptySpace = disk_map[dst]

    if file.length > space.length:
        raise Error(f'Not enough space. Needed {file.length}, got {space.length}')

    if file.length == space.length:
        disk_map[src], disk_map[dst] = disk_map[dst], disk_map[src]

        return

    remaining = space.length - file.length
    disk_map[dst] = file

    if remaining > 0:
        disk_map.insert(dst+1, EmptySpace(remaining))
        src += 1  # move cursor

    disk_map[src] = EmptySpace(file.length)

    # squash spaces
    # 1. before file (now space)
    if src > 0 and isinstance(disk_map[src - 1], EmptySpace):
        disk_map[src].length += disk_map[src - 1].length
        del disk_map[src - 1]
        src -= 1  # move cursor

    # 2. after
    if src + 1 != len(disk_map) and isinstance(disk_map[src + 1], EmptySpace):
        disk_map[src].length += disk_map[src + 1].length
        del disk_map[src + 1]


def checksum(disk_map):
    checksum = 0
    i = 0

    for data in disk_map:
        if isinstance(data, File):
            checksum += seq_sum(data.length, start=i) * data.id

        i += data.length

    return checksum


def solve_2(disk_map):
    processed_file_id = inf

    file_idx = len(disk_map) - 1  # to start from previous position, optimisation
    while processed_file_id > 0:
        while isinstance(disk_map[file_idx], EmptySpace) or disk_map[file_idx].id >= processed_file_id:
            file_idx -= 1

        processed_file_id = disk_map[file_idx].id

        space_idx = 0
        while (isinstance(disk_map[space_idx], File) or disk_map[space_idx].length < disk_map[file_idx].length) and space_idx < file_idx:
            space_idx += 1

        if space_idx < file_idx:
            move_file(disk_map, file_idx, space_idx)

    return checksum(disk_map)


if __name__ == '__main__':
    data, free_space, disk_map = parse_input('input.txt')

    print(f'Task 1: {solve_1(data, free_space)}')
    print(f'Task 2: {solve_2(disk_map)}')
