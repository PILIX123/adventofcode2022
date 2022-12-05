import re
inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day1/input1.txt"
input = open(inputpath, "r")
fixed = [[eval(y) for y in z] for z in [i.split("\n")
                                        for i in input.read().split("\n\n")]]


def part_one():
    biggest = 0
    for val in fixed:
        biggest = sum(val) if biggest < sum(val) else biggest
    return biggest


def part_two():
    biggest = [0, 0, 0]
    for val in fixed:
        if (biggest[0] < sum(val)):
            biggest[0] = sum(val)
        elif (biggest[1] < sum(val)):
            biggest[1] = sum(val)
        elif (biggest[2] < sum(val)):
            biggest[2] = sum(val)

    return sum(biggest)


print(part_one())
print(part_two())
