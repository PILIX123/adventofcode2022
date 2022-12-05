import re
inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day5/input.txt"
crate = "/Users/pierr/Desktop/Funny/adventofcode2022/day5/crate.txt"
# {letter: index for index, letter in enumerate(
#     list(string.ascii_letters), 1)}
input = open(inputpath, "r")
list_input = [re.findall(r'\d+', command)
              for command in input.read().split("\n")]
crates = {
    1: ['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],
    2: ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J'],
    3: ['F', 'B', 'H', 'W', 'P', 'M', 'Q'],
    4: ['V', 'S', 'T', 'D', 'F'],
    5: ['Q', 'L', 'D', 'W', 'V', 'F', 'Z'],
    6: ['Z', 'C', 'L', 'S'],
    7: ['Z', 'B', 'M', 'V', 'D', 'F'],
    8: ['T', 'J', 'B'],
    9: ['Q', 'N', 'B', 'G', 'L', 'S', 'P', 'H']
}
crates2 = {
    1: ['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],
    2: ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J'],
    3: ['F', 'B', 'H', 'W', 'P', 'M', 'Q'],
    4: ['V', 'S', 'T', 'D', 'F'],
    5: ['Q', 'L', 'D', 'W', 'V', 'F', 'Z'],
    6: ['Z', 'C', 'L', 'S'],
    7: ['Z', 'B', 'M', 'V', 'D', 'F'],
    8: ['T', 'J', 'B'],
    9: ['Q', 'N', 'B', 'G', 'L', 'S', 'P', 'H']
}


def part_one():
    output = ""
    for inputs in list_input:
        for x in range(0, eval(inputs[0])):
            crates.get(eval(inputs[2])).append(
                crates.get(eval(inputs[1])).pop())
    for crate in crates:
        output += crates[crate].pop()
    return output


def part_two():
    output = ""
    for inputs in list_input:
        crates2.get(eval(inputs[2])).extend(
            crates2.get(eval(inputs[1]))[-eval(inputs[0]):])
        for x in range(0, eval(inputs[0])):
            crates2.get(eval(inputs[1])).pop()
    for crate in crates2:
        output += crates2[crate].pop()
    return output


print(part_one())
print(part_two())
