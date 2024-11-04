import sys
import itertools

data = sys.stdin.read().splitlines()
galaxy_postions = [
    (x, y) for x in range(len(data)) for y in range(len(data[0]))
    if data[x][y] == "#"
]
bigger_rows = [i for i, d in enumerate(data) if all(p == "." for p in d)]
bigger_columns = [
    i for i, d in enumerate(map(list, zip(*data)))
    if all([p == "." for p in d])
]


def manhatan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 


def solver(multiplicator):
    final_distance = 0
    for a, b in itertools.combinations(galaxy_postions, r=2):
        distance = manhatan_distance(a, b)
        for br in bigger_rows:
            if a[0] < br < b[0] or b[0] < br < a[0]:
                distance += multiplicator - 1
        for bc in bigger_columns:
            if a[1] < bc < b[1] or b[1] < bc < a[1]:
                distance += multiplicator - 1
        final_distance += distance
    return final_distance

    
print("Task 1:", solver(2))
print("Task 2:", solver(1000000))

