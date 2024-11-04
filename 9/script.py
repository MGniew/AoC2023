import sys


def get_prediction(record, forward=True):
    stack = [record[:]]
    if not forward:
        stack = [list(reversed(record[:]))]

    while sum(stack[-1]) != 0:
        next_item = [b - a for a, b in zip(stack[-1][:-1], stack[-1][1:])]
        stack.append(next_item)
        
    diff = 0
    stack = list(reversed(stack))
    for next_id, item in enumerate(stack[:-1], 1):
        diff = stack[next_id][-1] + diff 
    return diff


data = [[int(r) for r in d.split()] for d in sys.stdin.read().splitlines()]
print("Task 1", sum(get_prediction(d) for d in data))
print("Task 2", sum(get_prediction(d, False) for d in data))

