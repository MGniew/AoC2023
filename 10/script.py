import sys
sys.setrecursionlimit(100000) 

import os
import time

mapping = {
    "|": {(1, 0): (1, 0), (-1, 0): (-1, 0)},
    "-": {(0, 1): (0, 1), (0, -1): (0, -1)},
    "L": {(1, 0): (0, 1), (0, -1): (-1, 0)},
    "J": {(0, 1): (-1, 0), (1, 0): (0, -1)},
    "7": {(0, 1): (1, 0), (-1, 0): (0, -1)},
    "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},
}

class Vector(tuple):

    def __add__(self, other):
        return Vector(a + b for a, b in zip(self, other))
    

def get_starting_pos(data):
    for x, d in enumerate(data):
        if (y := d.find("S")) > 0:
            return x, y


def find_initial_directions(spos, data, return_s_shape=False):
    directions = list()
    symbols = list()
    x, y = spos
    if data[x + 1][y] in "|LJ":
        directions.append((1, 0))
        symbols.append("|7F")
    if data[x - 1][y] in "|7F":
        directions.append((-1, 0))
        symbols.append("|LJ")
    if data[x][y + 1] in "-7J":
        directions.append((0, 1))
        symbols.append("-FL")
    if data[x][y - 1] in "-FL":
        directions.append((0, -1))
        symbols.append("-7J")


    symbol = set(symbols[0]).intersection(set(symbols[1]))
    if return_s_shape:
        return directions, symbol.pop()

    return directions



data = sys.stdin.read().splitlines()
spos = Vector(get_starting_pos(data))
directions = find_initial_directions(spos, data)
visited_nodes = [spos]
current_distance = 0
current_node = [spos, spos]
while True:
    print(current_node, directions)
    current_node[0] += directions[0]
    current_node[1] += directions[1]
    visited_nodes += current_node
    directions[0] = mapping[
        data[current_node[0][0]][current_node[0][1]]
    ][directions[0]]
    directions[1] = mapping[
        data[current_node[1][0]][current_node[1][1]]
    ][directions[1]] 
    current_distance += 1
    if current_node[0] == current_node[1]:
        break


print("Task 1:", current_distance)


class Area:
    shapes = {
        "|": [".x.", ".x.", ".x."],
        "-": ["...", "xxx", "..."],
        "L": [".x.", ".xx", "..."],
        "J": [".x.", "xx.", "..."],
        "7": ["...", "xx.", ".x."],
        "F": ["...", ".xx", ".x."],
        ".": ["...", "...", "..."],
    }

    def __init__(self):
        self.area = [["."] * 3 * len(data[0]) for _ in range(len(data) * 3)]

    def add_shape(self, shape, x, y):
        if shape == "S":
            _, shape = find_initial_directions((x, y), data, True)

        if (x, y) not in visited_nodes:
            shape = "."

        for i in range(x*3, x*3+3):
            for j in range(y*3, y*3+3):
                self.area[i][j] = self.shapes[shape][i - 3*x][j - 3*y]

    def __str__(self):
        result = ""
        for row in self.area:
            result += "".join(row) + "\n"
        return result

    def solve(self, x=0, y=0):
        if self.area[x][y] != ".":
            return
        print(self)
        os.system("clear")
        self.area[x][y] = "o"
        if x > 0:
            self.solve(x-1, y)
        if x < len(self.area) - 1:
            self.solve(x+1, y)
        if y > 0:
            self.solve(x, y-1)
        if y < len(self.area[0]) - 1:
            self.solve(x, y+1)


    def calculate_in_squares(self):
        counter = 0
        for x in range(0, len(self.area), 3):
            for y in range(0, len(self.area[0]), 3):
                symbols = self.area[x:x+3]
                symbols = [s[y:y+3] for s in symbols]
                if all(s == "." for row in symbols for s in row):
                    counter += 1

        return counter


area = Area()
for x, row in enumerate(data):
    for y, column in enumerate(row):
        area.add_shape(column, x, y)


area.solve()
print(area)
print("Task 2:", area.calculate_in_squares())



