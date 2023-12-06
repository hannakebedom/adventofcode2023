# Day 6: Wait for it (December 6th, 2023)

from utils import read_input
lines = read_input("day6ex.txt")

def day6():
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]

    for i in range(1, len(times)):
        time = int(times[i])
        distance = int(distances[i])
        for j in range(1, time):
            print(i)

    print("time: ", time)
    print("distance: ", distance)

day6()

