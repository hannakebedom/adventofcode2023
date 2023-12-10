# Day 9: Mirage Maintenance (December 10th, 2023)

from utils import read_input
lines = read_input("day9.txt")

def day9_p1():
    result = 0
    for line in lines:
        nums = [int(num) for num in line.split()]
        layers = [nums]

        # calculate layers
        while not all(num == 0 for num in layers[-1]):
            layer = []
            prev_layer = layers[-1]
            for i in range(len(layers[-1]) - 1):
                curr, next = prev_layer[i], prev_layer[i + 1]
                diff = next - curr
                layer.append(diff)
            layers.append(layer)

        # extrapolate
        prev = 0
        for layer in reversed(layers):
            prev = layer[-1] + prev
        result += prev

    return result


print(day9_p1())