inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day8/input.txt"
map = open(inputpath, "r").readlines()
# tree = [[int(c) for c in line] for line in map]


def part_one():
    total = 0
    previousTree = []
    nextTree = []
    for index, line in enumerate(map):
        if index == 0:
            total += len(map[index]) - 1
            previousTree.extend([[int(x) for x in tree]
                                for tree in map[index][:-1]])
            nextTree.extend([[int(x) for x in tree]
                            for tree in map[index+1][:-1]])
            for inde, _ in enumerate(nextTree):
                nextTree[inde].extend([eval(tree[inde])
                                      for tree in map[index+2:]])
            continue
        currentPreviousTrees = []
        currentNextTrees = [eval(tree) for tree in map[index][1:-1]]
        if (map[index] == map[-1]):
            total += len(map[index]) - 1
            continue
        for num, char in enumerate(line):
            if char == "\n":
                continue
            if num == 0:
                nextTree[num+1].pop(0)
                currentNextTrees.pop(0)

            if (num == 0 or line[num+1] == "\n"):
                previousTree[num].append(eval(char))
                currentPreviousTrees.append(eval(char))
                total += 1
                continue
            previousTrees = previousTree[num]
            nextTrees = nextTree[num]
            if eval(char) > max(previousTrees) or eval(char) > max(nextTrees) or eval(char) > max(currentNextTrees) or eval(char) > max(currentPreviousTrees):
                total += 1
            previousTree[num].append(eval(char))
            nextTree[num+1].pop(0)
            currentNextTrees.pop(0)
            currentPreviousTrees.append(eval(char))

    return (total)


def part_two():
    scenicScore = []
    previousTree = []
    nextTree = []

    for index, line in enumerate(map):
        if index == 0:
            previousTree.extend([[int(x) for x in tree]
                                for tree in map[index][:-1]])
            nextTree.extend([[int(x) for x in tree]
                            for tree in map[index+1][:-1]])
            for inde, _ in enumerate(nextTree):
                nextTree[inde].extend([eval(tree[inde])
                                       for tree in map[index+2:]])
        currentPreviousTrees = []
        currentNextTrees = [eval(tree) for tree in map[index][1:-1]]

        if (map[index] == map[-1] or index == 0):
            continue
        for num, treeLine in enumerate(line):
            leftVal = 0
            rightVal = 0
            topVal = 0
            downVal = 0
            if treeLine == "\n":
                continue
            if num == 0:
                nextTree[num+1].pop(0)
                currentNextTrees.pop(0)

            if (num == 0 or line[num+1] == "\n"):
                previousTree[num].append(eval(treeLine))
                currentPreviousTrees.append(eval(treeLine))

                continue
            #previousTrees = [eval(tree[num]) for tree in map[:index]]
            previousTrees = previousTree[num]
            nextTrees = nextTree[num]
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
            previousTrees.reverse()
            currentPreviousTrees.reverse()
            previousTree[num].append(eval(treeLine))
            nextTree[num+1].pop(0)
            currentNextTrees.pop(0)
            currentPreviousTrees.append(eval(treeLine))

    return max(scenicScore)


print(part_one())
print(part_two())
