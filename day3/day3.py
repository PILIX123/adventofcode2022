import re
import string
inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day3/input.txt"
input = open(inputpath, "r")
list_input = input.read().split("\n")
priority = {letter: index for index, letter in enumerate(
    list(string.ascii_letters), 1)}


def part_one():
    Total = 0
    for inputs in list_input:
        first_half = inputs[:int(len(inputs)/2)]
        second_half = inputs[int(len(inputs)/2):]
        for char in first_half:
            found = re.search(char, second_half)
            if (found != None):
                Total += priority.get(second_half[found.regs[0][0]])
                break
    return Total


def part_two():
    total = 0
    for index in range(0, len(list_input), 3):
        elf1 = list_input[index]
        elf2 = list_input[index+1]
        elf3 = list_input[index+2]
        for char in elf1:
            if (re.search(char, elf2) != None and re.search(char, elf3) != None):
                total += priority.get(char)
                break
    return total


print(part_one())
print(part_two())
