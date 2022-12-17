'''
u/West-Release-4842
https://www.reddit.com/user/West-Release-4842/
found from https://www.reddit.com/r/adventofcode/comments/zifqmh/comment/j0ci41b/?utm_source=share&utm_medium=web2x&context=3
=======================================================================
ADVENT OF CODE 2022 - Day 11: Monkey in the Middle
=======================================================================
'''
from functools import reduce
import operator
import time
inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day11/input.txt"


#Timing: Star
start = time.perf_counter()

# Load the data
file = open(inputpath, 'r')
input = [line.split() for line in file if line.strip() != '']


# Parse input
class Monkey:

    def __init__(self, id=0, items=None, ops=None, test=None, action=[]):
        self.id = id
        self.items = items
        self.ops = ops
        self.test = test
        self.action = action
        self.holds = 0

    def __str__(self):
        return f"{self.id} , {self.items} , {self.ops} , {self.test} , {self.action}"


def parse_input():
    monkeys = []
    for i in range(0, len(input) - 1, 6):
        for j in input[i:i + 6]:
            monkey = Monkey(id=int(input[i:i + 6][0][1].strip(":")))

            string = "".join(input[i:i + 6][1][2:])
            monkey.items = [int(s) for s in string.split(',')]

            monkey.ops = (input[i:i + 6][2][4], int(input[i:i + 6][2][5])
                          if input[i:i + 6][2][5] != "old" else "*2")

            monkey.test = int(input[i:i + 6][3][3])

            monkey.action = [int(input[i:i + 6][4][5]),
                             int(input[i:i + 6][5][5])]

            monkeys.append(monkey)

            break
    return monkeys


def operation(lvl, t_ops):
    if isinstance(t_ops[1], int):
        if t_ops[0] == '*':
            lvl *= t_ops[1]
        else:
            lvl += t_ops[1]
    else:
        lvl *= lvl

    return lvl


def solve(monkeys, rounds, part2=False):
    var = reduce(lambda accu, m: accu * m.test, monkeys, 1) if part2 else None
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.holds += len(monkey.items)

            for item in monkey.items:
                ops = operation(item, monkey.ops)
                ops = ops % var if part2 else ops // 3
                if ops % monkey.test == 0:
                    monkeys[monkey.action[0]].items.append(ops)
                else:
                    monkeys[monkey.action[1]].items.append(ops)

            monkey.items.clear()

    tmp = []
    [tmp.append(monkey.holds) for monkey in monkeys]
    tmp.sort()

    return tmp[-1] * tmp[-2]


# Main
monkeys = parse_input()
print("Part 1 answer: ", solve(monkeys, 20))

monkeys = parse_input()
print("Part 2 answer: ", solve(monkeys, 10000, part2=True))

#Timing: End
end = time.perf_counter()
print(f"\nTime to complete = {(end-start)*1000:.2f} milliseconds.")
