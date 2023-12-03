import sys
from dataclasses import dataclass
from collections import defaultdict
from functools import reduce


@dataclass
class Cubes:
    color: str
    num: int


def extract_turn(turn):
    result = list()
    hands = turn.split(",")
    for h in hands:
        num, color = h.strip().split(" ")
        result.append(Cubes(color=color, num=int(num)))
    return result


def is_game_ok(game):
    max_colors = {"red": 12, "green": 13, "blue": 14}
    for turn in game:
        color_nums = defaultdict(int)
        for hand in turn:
            color_nums[hand.color] += hand.num
        for k, v in color_nums.items():
            if max_colors[k] < color_nums[k]:
                return False
    return True
        

def get_game_power(game):
    min_colors = defaultdict(int)
    for turn in game:
        color_nums = defaultdict(int)
        for hand in turn:
            color_nums[hand.color] += hand.num
        for k, v in color_nums.items():
            if min_colors[k] < color_nums[k]:
                min_colors[k] = color_nums[k]
    return reduce(lambda x, y: x*y, min_colors.values())

data = sys.stdin.read().splitlines()
games = [s.split(":")[1].split(";") for s in data]
games = [[extract_turn(turn) for turn in g] for g in games]
games_ok = [is_game_ok(game) for game in games]
print("Task1:", sum([i for i, ok in enumerate(games_ok, start=1) if ok]))

games_powers = [get_game_power(game) for game in games]
print("Task2:", sum(games_powers))


