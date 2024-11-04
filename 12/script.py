import sys
from functools import lru_cache
from tqdm import tqdm

records = list()
groups = list()

data = sys.stdin.read().splitlines()
for line in data:
    line = line.split()
    records.append(line[0])
    groups.append([int(l) for l in line[1].split(",")])


def get_number_of_possible_arrangements(record, group):
    record = list(record)

    def solve(record, group, position=0, group_id=0, counter=0, started=False):
        record = list(record)
        group = list(group)
        n_solutions = 0
        current_group = group[group_id]
        for i in range(position, len(record)):
            match record[i]:
                case ".":
                    if counter < current_group and started:
                        return 0
                    if group_id + 1 < len(group) and started:
                        started = False
                        group_id += 1
                        counter = 0
                        current_group = group[group_id]
                case "#":
                    started = True
                    counter += 1
                    if counter > current_group:
                        return 0
                case "?": 
                    possible_record = record[:]
                    possible_record[i] = "."
                    n_solutions = solve(
                        tuple(possible_record), tuple(group),
                        position=i, group_id=group_id, counter=counter,
                        started=started
                    )
                    possible_record = record[:]
                    possible_record[i] = "#"
                    n_solutions += solve(
                        tuple(possible_record), tuple(group),
                        position=i, group_id=group_id, counter=counter,
                        started=started
                    )
                    return n_solutions

        if group_id == len(group) - 1 and counter == current_group:
            return 1
        return 0

    return solve(tuple(record), tuple(group))



result = 0
for i in range(len(groups)):
    result += get_number_of_possible_arrangements(records[i], groups[i])
print(result)


from joblib import Parallel, delayed


def solve(record, group):
    record = ((record + "?") * 5)[:-1]
    return get_number_of_possible_arrangements(record, group * 5)


result = Parallel(n_jobs=-1)(
    delayed(solve)(records[i], groups[i]) for i in tqdm(range(len(groups)))
)

print(sum(result))
