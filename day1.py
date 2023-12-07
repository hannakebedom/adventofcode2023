# Day 1: Trebuchet?! (December 4th, 2023)

from utils import read_input
lines = read_input("day1.txt")

# Part 1
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

# Part 2
DIGITS = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
def sum_calibration_letter_digits():
    sum = 0
    
    for line in lines:
        first = ''
        last = ''
        i = 0

        while i < len(line) - 1:
            char = line[i]

            if char.isnumeric() and not first:
                first = char
                i += 1
            elif char.isnumeric() and first:
                last = char
                i += 1
            elif char.isalpha():
                num = 0
                if DIGITS.get(line[i:i+3]):
                    num = DIGITS.get(line[i:i+3])
                    i += 2
                elif DIGITS.get(line[i:i+4]):
                    num = DIGITS.get(line[i:i+4])
                    i += 3
                elif DIGITS.get(line[i:i+5]):
                    num = DIGITS.get(line[i:i+5])
                    i += 4
                else:
                    i += 1
                    continue
                
                if not first:
                    first = num
                else:
                    last = num

        if first and last:
            number = first + last
        else:
            number = first + first
        
        sum += int(number)

    return sum

print("result (part 2): ", sum_calibration_letter_digits())

