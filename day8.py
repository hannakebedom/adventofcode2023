# Day 8: Haunted Wasteland (December 8th, 2023)

import re
from utils import read_input
lines = read_input("day8ex3.txt")

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


def day8_p2():
    network = {}
    instructions = lines[0].strip()
    starting_nodes = []

    # build network
    for i in range(2, len(lines)):
        parts = re.split(r'\s*=\s*', lines[i])
        key = parts[0]
        if key.endswith("A"):
            starting_nodes.append(key)
        value = re.sub(r'[()]', '', parts[1]).split(',')
        value = [item.strip() for item in value]
        network[key] = value

    print("starting nodes: ", starting_nodes)

    # traverse network
    # cycles ??
    curr_nodes = starting_nodes
    steps = 1
    found = False

    while found == False:
        next_nodes = []
        for instruction in instructions:
            for node in curr_nodes:
                print("node: ", node)
                if instruction == "R":
                    curr = network[node][1]
                else:
                    curr = network[node][0]
                
                next_nodes.append(curr)
            print("next_nodes: ", next_nodes)
            print("steps: ", steps)
            steps += 1
            curr_nodes = next_nodes
            if all(item.endswith("Z") for item in curr_nodes):
                return steps

    # curr = network["AAA"]
    # steps = 1
    # found = False

    # while found == False:
    #     for instruction in instructions:

    #         if instruction == "R":
    #             if curr[1] == "ZZZ":
    #                 return steps
    #             curr = network[curr[1]]
    #         else:
    #             if curr[0] == "ZZZ":
    #                 return steps
    #             curr = network[curr[0]]

    #         steps += 1

    #     if steps == 6:
    #         break

    # return steps

print(day8_p2())
