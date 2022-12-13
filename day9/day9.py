inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day9/input.txt"

data = [lines.split(" ") for lines in open(inputpath).read().splitlines()]
idea = [["" for _ in range(26)] for _ in range(26)]
"""
if next direction is opposite to current, tail doesnt move
if head and tail on same axis of direction both move
if head and tail on perpendicular axis of direction, tail doesnt move
if diagonal, direction away from tail tail takes head place
if diagonal, direction next to tail, tail doesnt move
"""
val = 1
vlaue = 1

visited = {}


class Head():
    def __init__(self) -> None:
        self.y = 0
        self.x = 0

    def move(self, direction, movement):
        match direction:
            case "U":
                self.y += movement
            case "D":
                self.y -= movement
            case "L":
                self.x -= movement
            case "R":
                self.x += movement


class Tail():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.distance = 0
        self.movements = []

    def move(self, direction, movement, length, head):
        h_distance = (head.x-self.x)
        v_distance = (head.y-self.y)
        prevy = self.y
        prevx = self.x
        l_coord = []
        match direction:
            case "U":
                if (self.y+length >= head.y):
                    return
                elif (self.y >= head.y - movement):
                    self.y += v_distance-length
                else:
                    self.y += movement

                if (self.x < head.x):
                    self.x += 1
                elif (self.x > head.x):
                    self.x -= 1

                if (self.y != prevy or self.x != prevx):
                    l_coord = [(self.x, y) for y in range(prevy+1, self.y + 1)]
                    for coord in l_coord:
                        visit = {str(coord): "visited"}
                        visited.update(visit)

            case "D":
                if (self.y-length <= head.y):
                    return
                elif (self.y <= head.y + movement):
                    self.y -= (-v_distance)-length
                else:
                    self.y -= movement

                if (self.x < head.x):
                    self.x += 1
                elif (self.x > head.x):
                    self.x -= 1

                if (self.y != prevy or self.x != prevx):
                    l_coord = [(self.x, y)
                               for y in range(prevy-1, self.y - 1, -1)]
                    for coord in l_coord:
                        visit = {str(coord): "visited"}
                        visited.update(visit)

            case "R":
                if (self.x+length >= head.x):
                    return
                elif (self.x >= head.x - movement):
                    self.x += h_distance-length
                else:
                    self.x += movement

                if (self.y < head.y):
                    self.y += 1
                elif (self.y > head.y):
                    self.y -= 1

                if (prevx != self.x or self.x != prevx):
                    l_coord = [(x, self.y) for x in range(prevx+1, self.x + 1)]
                    for coord in l_coord:
                        visit = {str(coord): "visited"}
                        visited.update(visit)
            case "L":
                if (self.x-length <= head.x):
                    return
                elif (self.x <= head.x + movement):
                    self.x -= (-h_distance)-length
                else:
                    self.x -= movement

                if (self.y < head.y):
                    self.y += 1
                elif (self.y > head.y):
                    self.y -= 1

                if (prevx != self.x or self.x != prevx):
                    l_coord = [(x, self.y)
                               for x in range(prevx-1, self.x - 1, -1)]
                    for coord in l_coord:
                        visit = {str(coord): "visited"}
                        visited.update(visit)


class Knot():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.distance = 0
        self.movements = []

    def move(self, direction, movement, length, head):
        h_distance = (head.x-self.x)
        v_distance = (head.y-self.y)
        prevy = self.y
        prevx = self.x
        l_coord = []
        match direction:
            case "U":
                if (self.y+length >= head.y):
                    return
                elif (self.y >= head.y - movement):
                    self.y += v_distance-length
                else:
                    self.y += movement

                if (self.x < head.x):
                    self.x += 1
                elif (self.x > head.x):
                    self.x -= 1

            case "D":
                if (self.y-length <= head.y):
                    return
                elif (self.y <= head.y + movement):
                    self.y -= (-v_distance)-length
                else:
                    self.y -= movement

                if (self.x < head.x):
                    self.x += 1
                elif (self.x > head.x):
                    self.x -= 1

            case "R":
                if (self.x+length >= head.x):
                    return
                elif (self.x >= head.x - movement):
                    self.x += h_distance-length
                else:
                    self.x += movement

                if (self.y < head.y):
                    self.y += 1
                elif (self.y > head.y):
                    self.y -= 1

            case "L":
                if (self.x-length <= head.x):
                    return
                elif (self.x <= head.x + movement):
                    self.x -= (-h_distance)-length
                else:
                    self.x -= movement

                if (self.y < head.y):
                    self.y += 1
                elif (self.y > head.y):
                    self.y -= 1


head = Head()
tail = Tail()
visit = {str((tail.x, tail.y)): "visited"}
visited.update(visit)


def part_one(length):
    for instruction in data:
        head.move(instruction[0], int(instruction[1]))
        tail.move(instruction[0], int(instruction[1]), length, head)
    return (len(visited))


def part_two():
    l_instruction = []
    for instruction in data:
        l_instruction.append(instruction)
        if (len(l_instruction) > 10):
            l_instruction.pop(0)

        head.move(l_instruction[0][0], int(l_instruction[0][1]))
        for index, knots in enumerate(l_knot):
            if (index == 0):
                knots.move(l_instruction[index][0],
                           int(l_instruction[index][1]), 1, head)
            else:
                if (index > len(l_instruction)-1):
                    continue
                knots.move(l_instruction[index][0], int(
                    l_instruction[index][1]), 1, l_knot[index-1])
        if (9 > len(l_instruction)-1):
            continue
        tail.move(l_instruction[9][0], int(l_instruction[9][1]), 1, l_knot[-1])
    return (len(visited))


print(part_one(1))
head = Head()
tail = Tail()
l_knot = [Knot() for _ in range(0, 9)]

visited.clear()
visit = {str((tail.x, tail.y)): "visited"}
visited.update(visit)


print(part_two())
