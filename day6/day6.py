import re

inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day6/input.txt"
inputstring = open(inputpath, "r").read()


def create_regex(length):
    regex = '((\w)'
    for i in range(1, length):
        regex += '('
        for j in range(2, i+2):
            regex += f'(?!\{j})'
        regex += '\w)'
    regex += ")"
    return (regex)


def part_one():
    regex = create_regex(4)
    return (re.search(regex, inputstring).regs[0][1])


def part_two():
    regex = create_regex(14)
    return (re.search(regex, inputstring).regs[0][1])


print(part_one())
print(part_two())
