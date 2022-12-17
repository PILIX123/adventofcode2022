monkeys = {
    'monkey0': [84, 72, 58, 51],
    "monkey1": [88, 58, 58],
    'monkey2': [93, 82, 71, 77, 83, 53, 71, 89],
    'monkey3': [81, 68, 65, 81, 73, 77, 96],
    'monkey4': [75, 80, 50, 73, 88],
    'monkey5': [59, 72, 99, 87, 91, 81],
    'monkey6': [86, 69],
    'monkey7': [91]
}


class Monkey:
    def __init__(self, name, trueMonkey, falseMonkey, action: str, testValue: int) -> None:
        self.name = name
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.action = action.split(" ")
        self.action.pop(0)
        self.testValue = testValue
        self.inspection = 0

    def bored(self):
        monkeys[self.name][0] = int(monkeys[self.name][0]/3)

    def test(self):
        return monkeys[self.name][0] % self.testValue == 0

    def throw(self, resultTest: bool):
        if resultTest:
            monkeys[self.trueMonkey].append(monkeys[self.name][0])
        else:
            monkeys[self.falseMonkey].append(monkeys[self.name][0])
        monkeys[self.name].pop(0)

    def operation(self):
        number = monkeys[self.name][0] if "old" in self.action else int(
            self.action[1])
        if "*" in self.action:
            monkeys[self.name][0] = monkeys[self.name][0]*number
        elif "+" in self.action:
            monkeys[self.name][0] = monkeys[self.name][0]+number

    def turn(self):
        for _ in range(len(monkeys[self.name])):
            self.operation()
            self.inspection += 1
            self.bored()
            self.throw(self.test())

    def turnv2(self):
        for _ in range(len(monkeys[self.name])):
            self.operation()
            self.inspection += 1
            self.throw(self.test())


monkey0 = Monkey('monkey0', 'monkey1', 'monkey7', 'old * 3', 13)
monkey1 = Monkey('monkey1', 'monkey7', 'monkey5', 'old + 8', 2)
monkey2 = Monkey('monkey2', 'monkey3', 'monkey4', 'old * old', 7)
monkey3 = Monkey('monkey3', 'monkey4', 'monkey6', 'old + 2', 17)
monkey4 = Monkey('monkey4', 'monkey6', 'monkey0', 'old + 3', 5)
monkey5 = Monkey('monkey5', 'monkey2', 'monkey3', 'old * 17', 11)
monkey6 = Monkey('monkey6', 'monkey1', 'monkey0', 'old + 6', 3)
monkey7 = Monkey('monkey7', 'monkey2', 'monkey5', 'old + 1', 19)
monkeyList = [monkey0, monkey1, monkey2,
              monkey3, monkey4, monkey5, monkey6, monkey7]


def part_one():
    for _ in range(20):
        monkey0.turn()
        monkey1.turn()
        monkey2.turn()
        monkey3.turn()
        monkey4.turn()
        monkey5.turn()
        monkey6.turn()
        monkey7.turn()
    inspections = [monkey.inspection for monkey in monkeyList]
    inspections.sort()
    return (inspections[6]*inspections[7])


# print(part_one())
def part_two():
    for _ in range(10000):
        monkey0.turnv2()
        monkey1.turnv2()
        monkey2.turnv2()
        monkey3.turnv2()
        monkey4.turnv2()
        monkey5.turnv2()
        monkey6.turnv2()
        monkey7.turnv2()
    inspections = [monkey.inspection for monkey in monkeyList]
    inspections.sort()
    return (inspections[6]*inspections[7])


print(part_one())
monkeys = {
    'monkey0': [84, 72, 58, 51],
    "monkey1": [88, 58, 58],
    'monkey2': [93, 82, 71, 77, 83, 53, 71, 89],
    'monkey3': [81, 68, 65, 81, 73, 77, 96],
    'monkey4': [75, 80, 50, 73, 88],
    'monkey5': [59, 72, 99, 87, 91, 81],
    'monkey6': [86, 69],
    'monkey7': [91]
}

monkey0 = Monkey('monkey0', 'monkey1', 'monkey7', 'old * 3', 13)
monkey1 = Monkey('monkey1', 'monkey7', 'monkey5', 'old + 8', 2)
monkey2 = Monkey('monkey2', 'monkey3', 'monkey4', 'old * old', 7)
monkey3 = Monkey('monkey3', 'monkey4', 'monkey6', 'old + 2', 17)
monkey4 = Monkey('monkey4', 'monkey6', 'monkey0', 'old + 3', 5)
monkey5 = Monkey('monkey5', 'monkey2', 'monkey3', 'old * 17', 11)
monkey6 = Monkey('monkey6', 'monkey1', 'monkey0', 'old + 6', 3)
monkey7 = Monkey('monkey7', 'monkey2', 'monkey5', 'old + 1', 19)

print(part_two())
