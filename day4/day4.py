import re
inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day4/input.txt"
input = open(inputpath, "r")
list_input = [[y.split("-") for y in x.split(",")]
              for x in input.read().split("\n")]


def part_one():
    total = 0
    for inputs in list_input:
        if ((eval(inputs[0][0]) <= eval(inputs[1][0])) and (eval(inputs[0][1]) >= eval(inputs[1][1]))) or ((eval(inputs[0][0]) >= eval(inputs[1][0])) and (eval(inputs[0][1]) <= eval(inputs[1][1]))):
            total += 1
    return total


def part_two():
    total = 0
    for inputs in list_input:
        if ((eval(inputs[0][0]) <= eval(inputs[1][0])) and (eval(inputs[0][1]) >= eval(inputs[1][0]))) or ((eval(inputs[0][0]) >= eval(inputs[1][0])) and (eval(inputs[0][0]) <= eval(inputs[1][1]))):
            total += 1
    return total


print(part_two())
