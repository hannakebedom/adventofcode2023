# Day 1: Trebuchet?! (December 4th, 2023)

file = open('input/day1.txt', 'r')
lines = file.readlines()

def sum_calibration_values():
    sum = 0
    for line in lines:
        first = ''
        last = ''

        for char in line:
            if char.isnumeric() and not first:
                first = char
            elif char.isnumeric() and first:
                last = char

        if first and last:
            num = first + last
        else:
            num = first + first

        print("number: ", num)
        sum += int(num)
    return sum

print("result: ", sum_calibration_values())
            
