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
    def __init__(self, items: list, trueMonkey, falseMonkey, action: str, testValue: int) -> None:
        self.items = items
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.action = action.split(" ")
        self.action.pop(0)
        self.testValue = testValue
        self.inspection = 0

    def bored(self):
        self.items[0] = int(self.items[0]/3)

    def test(self):
        return self.items[0] % self.testValue == 0

    def throw(self, resultTest: bool):
        if resultTest:
            monkeys[self.trueMonkey].append(self.items[0])
        else:
            monkeys[self.falseMonkey].append(self.items[0])
        self.items.pop(0)

    def operation(self):
        number = self.items[0] if "old" in self.action else int(self.action[1])
        if "*" in self.action:
            self.items[0] = self.items[0]*number
        elif "+" in self.action:
            self.items[0] = self.items[0]+number

    def turn(self, items):
        self.items = items
        for _ in range(len(self.items)):
            self.operation()
            self.inspection += 1
            self.bored()
            self.throw(self.test())


monkey0 = Monkey(monkeys['monkey0'], 'monkey1', 'monkey7', 'old * 3', 13)
monkey1 = Monkey(monkeys['monkey1'], 'monkey7', 'monkey5', 'old + 8', 2)
monkey2 = Monkey(monkeys['monkey2'], 'monkey3', 'monkey4', 'old * old', 7)
monkey3 = Monkey(monkeys['monkey3'], 'monkey4', 'monkey6', 'old + 2', 17)
monkey4 = Monkey(monkeys['monkey4'], 'monkey6', 'monkey0', 'old + 3', 5)
monkey5 = Monkey(monkeys['monkey5'], 'monkey2', 'monkey3', 'old * 17', 11)
monkey6 = Monkey(monkeys['monkey6'], 'monkey1', 'monkey0', 'old + 6', 3)
monkey7 = Monkey(monkeys['monkey7'], 'monkey2', 'monkey5', 'old + 1', 19)
monkeyList = [monkey0, monkey1, monkey2,
              monkey3, monkey4, monkey5, monkey6, monkey7]
for _ in range(20):
    monkey0.turn(monkeys['monkey0'])
    monkey1.turn(monkeys['monkey1'])
    monkey2.turn(monkeys['monkey2'])
    monkey3.turn(monkeys['monkey3'])
    monkey4.turn(monkeys['monkey4'])
    monkey5.turn(monkeys['monkey5'])
    monkey6.turn(monkeys['monkey6'])
    monkey7.turn(monkeys['monkey7'])
inspections = [monkey.inspection for monkey in monkeyList]
inspections.sort()
print(inspections[6]*inspections[7])
