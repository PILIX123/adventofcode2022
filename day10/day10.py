inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day10/input.txt"
actions = [lines.split(" ")
           for lines in open(inputpath, "r").read().splitlines()]
cycle = 1
index = 0
register = 1
currentcyle = []
numbers = 0
while cycle < 241:
    if actions[index][0] == 'noop':
        if len(currentcyle) == 1:
            index += 1
            currentcyle.clear()
            continue
        else:
            currentcyle.append(cycle)
    if actions[index][0] == 'addx':
        if len(currentcyle) == 2:
            register += int(actions[index][1])
            index += 1
            currentcyle.clear()
            continue
        else:
            currentcyle.append(cycle)
    if cycle % 40 == 20:
        numbers += cycle*register
    if (((cycle-1) % 40) == register+1 or ((cycle-1) % 40) == register or ((cycle-1) % 40) == register-1):
        print('#', end='')
    else:
        print(' ', end='')
    if (cycle % 40 == 0):
        print('')
    cycle += 1
print(numbers)
