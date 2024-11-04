import sys


class CustomMap:

    def __init__(self):
        self.src = list()
        self.dst = list()
        self.offset = list()

    def __getitem__(self, key):
        if isinstance(key, tuple):
            s, o = key
            results = list()
            for i, src in enumerate(self.src):
                if src

                if (
                    src <= s < src + self.offset[i] or
                    src <= s + o <= src+self.offset[i]
                ):
                    results.append((self.dst[i], self.offset[i]))
            return results

        for i, src in enumerate(self.src):
            if src <= key < src + self.offset[i]:
                current_offset = key - src
                return self.dst[i] + current_offset
        return key

    def set_record(self, src, dst, offset):
        self.src.append(src)
        self.dst.append(dst)
        self.offset.append(offset)

    def get_ordered_mapping(self):
        s, o = zip(*sorted(zip(self.src, self.offset)))
        return s, o


def parse_input(data):
    seeds = [int(s) for s in data.pop(0).split(":")[1].split()]
    result = dict()
    for d in data:
        if "map" in d:
            map_name = d.split(" ")[0]
            result[map_name] = CustomMap()
        elif d:
            dst, src, offset = d.strip().split()
            result[map_name].set_record(int(src), int(dst), int(offset))
    return seeds, result
 

def solve_part1(seeds, maps):
    locations = list()
    for s in seeds:
        for name, mapping in maps.items():
            s = mapping[s]
        locations.append(s)
    return min(locations)


def solve_part2(seeds, maps):

    for s, o in zip(seeds[::2], seeds[1::2]):
        tasks = [(s, o)]
        new_tasks = list()
        for name, mapping in maps.items():
            for s, o in tasks:
                new_tasks += mapping[s, o]

            tasks = new_tasks
            new_tasks = list()

    return tasks



seeds, maps = parse_input(sys.stdin.read().splitlines())
print("Task 1:", solve_part1(seeds, maps))
print("Task 2:", solve_part2(seeds, maps))
