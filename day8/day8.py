inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day8/input.txt"
map = open(inputpath, "r").readlines()
#tree = [[int(c) for c in line] for line in map]
total = 0


def part_one():
    for index, line in enumerate(map):
        if (map[index] == map[-1] or index == 0):
            total += len(map[index]) - 1
            continue
        for num, char in enumerate(line):
            if char == "\n":
                continue
            if (num == 0 or line[num+1] == "\n"):
                total += 1
                continue

            previousTrees = [eval(tree[num]) for tree in map[:index]]
            nextTrees = [eval(tree[num]) for tree in map[index+1:]]
            currentPreviousTrees = [eval(num) for num in list(line[:num])]
            currentNextTrees = [eval(num) for num in list(line[num+1:-1])]
            if eval(char) > max(previousTrees) or eval(char) > max(nextTrees) or eval(char) > max(currentNextTrees) or eval(char) > max(currentPreviousTrees):
                total += 1
    return (total)


print(part_one())
