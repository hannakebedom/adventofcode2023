# Day 2: Cube Conundrum (December 6th, 2023)

from utils import read_input
lines = read_input("day2.txt")

MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

def day2_p1():
    result = 0

    for line in lines:
        game = line.split(":")
        id = int(game[0].split()[1])
        sets = game[1].split(";")
        game_possible = True

        for set in sets:
            for cubes in set.split(","):
                count, colour = cubes.split()
                if int(count) > MAX_CUBES[colour]:
                    game_possible = False
        
        if game_possible:
            result += id
        
    return result

print(day2_p1())

def day2_p2():
    result = 0

    for line in lines:
        game = line.split(":")
        sets = game[1].split(";")
        minimum_set = {"red": 0, "green": 0, "blue": 0}

        for set in sets:
            for cubes in set.split(","):
                count, colour = cubes.split()
                if int(count) > minimum_set[colour]:
                    minimum_set[colour] = int(count)
        
        power = minimum_set["red"] * minimum_set["green"] * minimum_set["blue"]
        
        result += power
        
    return result

        
print(day2_p2())




