inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day10/input.txt"
actions = [lines.split(" ")
           for lines in open(inputpath, "r").read().splitlines()]
cycle = 1
index = 0
register = 1
currentcyle = 0
while cycle < 221:
    if actions[index] == "noop":
        index += 1
    if actions[index] == "addx":
        currentcyle = cycle
    cycle += 1
