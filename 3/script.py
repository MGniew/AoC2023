import sys
from itertools import product
from collections import defaultdict


def part_number_generator(data):
    
    def is_part_number(start_pos, num_length, data):
        invalid_symbols = "0123456789."
        i, j = start_pos
        bound = (
            list(product([i-1, i+1], range(j-1, j+num_length+1))) + 
            [(i, j-1), (i, j + num_length)]
        )
        for x, y in bound:
            if (
                len(data) > x >= 0 and 
                len(data[0]) > y >= 0 and 
                data[x][y] not in invalid_symbols
            ):
                return True
        return False

    current_number = ""
    for i, line in enumerate(data):
        if current_number:
            if is_part_number(
                number_starting_pos,
                len(current_number),
                data
            ):
                yield int(current_number)
        current_number = ""
        for j, char in enumerate(line):
            if char in "0123456789":
                if not current_number:
                    number_starting_pos = (i, j)
                current_number += char
            elif current_number:
                if is_part_number(
                    number_starting_pos,
                    len(current_number),
                    data
                ):
                    yield int(current_number)
                current_number = ""


def ratio_generator(data):
    def get_gears_positions(start_pos, num_length, data):
        i, j = start_pos
        gear_positions = []
        bound = (
            list(product([i-1, i+1], range(j-1, j+num_length+1))) + 
            [(i, j-1), (i, j + num_length)]
        )
        for x, y in bound:
            if (
                len(data) > x >= 0 and 
                len(data[0]) > y >= 0 and 
                data[x][y] == "*"
            ):
                gear_positions.append((x, y))
        return gear_positions

    current_number = ""
    gear_to_numbers = defaultdict(list)
    for i, line in enumerate(data):
        if current_number:
            gears = get_gears_positions(
                number_starting_pos,
                len(current_number),
                data
            )
            for gear in gears:
                gear_to_numbers[gear].append(int(current_number))
        current_number = ""
        for j, char in enumerate(line):
            if char in "0123456789":
                if not current_number:
                    number_starting_pos = (i, j)
                current_number += char
            elif current_number:
                gears = get_gears_positions(
                    number_starting_pos,
                    len(current_number),
                    data
                )
                for gear in gears:
                    gear_to_numbers[gear].append(int(current_number))
                current_number = ""

    for k, v in gear_to_numbers.items():
        if len(v) > 1:
            yield v[0] * v[1]



data = sys.stdin.read().splitlines()
print("Task 1:", sum(part_number_generator(data)))
print("Task 2:", sum(ratio_generator(data)))
