import sys


def parse_input(data):
    data = [d.split(":")[1].split("|") for d in data]
    winning = [[int(num) for num in d[0].split(" ") if num] for d in data]
    lottery_numbers = [[int(num) for num in d[1].split(" ") if num] for d in data]
    return winning, lottery_numbers


def solve_part1(winning, lottery_numbers):
    total_points = 0
    for w, l in zip(winning, lottery_numbers):
        w = set(w)
        l = set(l)
        common = w & l
        if len(common) > 0:
            points = 2**(len(common) - 1)
            total_points += points

    return total_points


def solve_part2(winning, lottery_numbers):
    copies = [1] * len(winning)
    for i, l in enumerate(lottery_numbers):
        w = set(winning[i])
        l = set(l)
        common = w & l
        num_wins = len(common)
        for nw in range(num_wins):
            if i + nw + 1 < len(copies):
                copies[i + nw + 1] += copies[i]

    return sum(copies)


data = sys.stdin.read().splitlines()
winning, lottery_numbers = parse_input(data)
print("Task 1:", solve_part1(winning, lottery_numbers))
print("Task 2:", solve_part2(winning, lottery_numbers))
