# Day 8: Haunted Wasteland (December 8th, 2023)

import re
from utils import read_input
lines = read_input("day8.txt")

def day8_p1():
    network = {}
    instructions = lines[0].strip()

    # build network
    for i in range(2, len(lines)):
        parts = re.split(r'\s*=\s*', lines[i])
        key = parts[0]
        value = re.sub(r'[()]', '', parts[1]).split(',')
        value = [item.strip() for item in value]
        network[key] = value

    # traverse network
    curr = network["AAA"]
    steps = 1
    found = False

    while found == False:
        for instruction in instructions:
            if instruction == "R":
                if curr[1] == "ZZZ":
                    return steps
                curr = network[curr[1]]
            else:
                if curr[0] == "ZZZ":
                    return steps
                curr = network[curr[0]]

            steps += 1

        if steps == 6:
            break

    return steps

print(day8_p1())
