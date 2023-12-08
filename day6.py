# Day 6: Wait for it (December 6th, 2023)

from utils import read_input
lines = read_input("day6.txt")

def day6_p1():
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]

    result = 1
    for i in range(len(times)):
        time = int(times[i])
        record_distance = int(distances[i])
        ways_to_beat_record = 0

        print("race")
        print("time: ", time)
        print("record distance: ", record_distance)

        for j in range(1, time):
            speed = j # in mm per ms
            remaining_time = time - j # in ms
            distance = speed * remaining_time # in mm
            if distance > record_distance:
                ways_to_beat_record += 1

        result *= ways_to_beat_record

    return result

print(day6_p1())

def day6_p2():
    time = int("".join(lines[0].split()[1:]))
    record_distance = int("".join(lines[1].split()[1:]))
    ways_to_beat_record = 0

    for j in range(1, time):
        speed = j # in mm per ms
        remaining_time = time - j # in ms
        distance = speed * remaining_time # in mm
        if distance > record_distance:
            ways_to_beat_record += 1

    return ways_to_beat_record

print(day6_p2())





