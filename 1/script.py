import sys
from itertools import product

data = sys.stdin.read().splitlines()
numbers = ["".join([char for char in s if char and char.isdigit()]) for s in data]
numbers = ([int(s[0] + s[-1]) for s in numbers if s])
print("Task1:", sum(numbers))


mapping = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
mapping = {digit: str(i+1) for i, digit in enumerate(mapping)}
numbers = []
for s in data:
    order = []
    for k, v in mapping.items():
        for value, fun in product([k, v], [str.find, str.rfind]):
            if (pos := fun(s, value)) >= 0:
                order.append((pos, mapping.get(value, value)))
    order = sorted(order, key=lambda x: x[0])
    number = int(order[0][1] + order[-1][1])
    numbers.append(number)

print("Task2:", sum(numbers))



