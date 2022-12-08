inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day8/input.txt"
map = open(inputpath, "r").readlines()
# tree = [[int(c) for c in line] for line in map]
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


def part_two():
    scenicScore = []
    for index, line in enumerate(map):

        if (map[index] == map[-1] or index == 0):
            continue
        for num, treeLine in enumerate(line):
            leftVal = 0
            rightVal = 0
            topVal = 0
            downVal = 0

            if (num == 0 or treeLine == "\n" or line[num+1] == "\n"):
                continue
            previousTrees = [eval(tree[num]) for tree in map[:index]]
            nextTrees = [eval(tree[num]) for tree in map[index+1:]]
            currentPreviousTrees = [eval(num) for num in list(line[:num])]
            currentNextTrees = [eval(num) for num in list(line[num+1:-1])]
            previousTrees.reverse()
            currentPreviousTrees.reverse()
            for trees in currentPreviousTrees:
                if eval(treeLine) <= trees:
                    leftVal += 1
                    break
                leftVal += 1
            for trees in previousTrees:
                if eval(treeLine) <= trees:
                    topVal += 1
                    break
                topVal += 1
            for trees in nextTrees:
                if eval(treeLine) <= trees:
                    downVal += 1
                    break
                downVal += 1
            for trees in currentNextTrees:
                if eval(treeLine) <= trees:
                    rightVal += 1
                    break
                rightVal += 1
            scenicScore.append(leftVal*rightVal*topVal*downVal)
    return max(scenicScore)


print(part_two())
