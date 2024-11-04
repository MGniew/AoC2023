import sys


def move_generator(moves):
    while True:
        for move in moves:
            yield move


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a / gcd(a, b)) * b

data = sys.stdin.read().splitlines()
moves = data[0]
nodes = {
    d[0].strip(): {
        "L": d[1][0].strip(),
        "R": d[1][1].strip()} 
    for d in [
        [d[0], d[1].split(",")] 
        for d in [
            d.replace("(", "").replace(")", "").split("=") for d in data[2:]
        ]
    ]
}



current_node = "AAA"
stop_node = "ZZZ"
move = move_generator(moves)
counter = 0
while current_node != stop_node:
    current_node = nodes[current_node][next(move)]
    counter += 1
print("Task 1", counter)


move = move_generator(moves)
current_nodes = [(d, d) for d in nodes.keys() if d.endswith("A")]
counters = {s: 0 for s, c in current_nodes}
while current_nodes:
    m = next(move)
    current_nodes = [(s, nodes[c][m]) for s, c in current_nodes]
    for s, c in current_nodes:
        counters[s] += 1
    current_nodes = [(s, c) for s, c in current_nodes if not c.endswith("Z")]

current = 1
for counter in counters.values():
    current = lcm(current, counter)
print("Task 2", int(current))
