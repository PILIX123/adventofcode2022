inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day9/input.txt"

data = [lines.split(" ") for lines in open(inputpath).read().splitlines()]
idea = [["" for _ in range(100)] for _ in range(100)]
"""
if next direction is opposite to current, tail doesnt move
if head and tail on same axis of direction both move
if head and tail on perpendicular axis of direction, tail doesnt move
if diagonal, direction away from tail tail takes head place
if diagonal, direction next to tail, tail doesnt move
"""

visited = {}


class Head():
    def __init__(self) -> None:
        self.y = 0
        self.x = 0

    def move(self, direction, movement):
        idea[self.y][self.x] == ""
        match direction:
            case "U":
                self.y += movement
            case "D":
                self.y -= movement
            case "L":
                self.x -= movement
            case "R":
                self.x += movement
        idea[self.y][self.x] = "H"


class Tail():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move(self, direction, movement, head: Head):
        if head.x == self.x:
            if self.y > head.y:
                if direction != "D":
                    return
                self.x -= movement
            elif self.y < head.y:
                if direction != "U":
                    return
                self.x += movement
            else:
                return
        if head.y == self.y:
            if self.x > head.x:
                if direction != "L":
                    return
                self.x -= movement


head = Head()

for index, instruction in enumerate(data):
    if (instruction[0] == data[index+1][0]):
        Head.move(head, instruction[0], int(instruction[1]))
