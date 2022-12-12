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
val = str((1, 2))


class Head():
    def __init__(self) -> None:
        self.y = 0
        self.x = 0

    def move(self, direction, movement, tail):
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

    def move(self, direction, movement, length, head: Head):
        if head.x == self.x:
            if self.y > head.y+length:
                if direction != "D":
                    return
                self.y -= movement
            elif self.y < head.y-length:
                if direction != "U":
                    return
                self.y += movement
            coordinates = {str((self.x, self.y)): "visited"}
            visited.update(coordinates)
            return
        if head.y == self.y:
            if self.x > head.x+length:
                if direction != "L":
                    return
                self.x -= movement
            elif self.x < head.x-length:
                if direction != "R":
                    return
                self.x += movement
            coordinates = {str((self.x, self.y)): "visited"}
            visited.update(coordinates)
            return


head = Head()
tail = Tail()


for instruction in data:
    head.move(instruction[0], int(instruction[1]))
    tail.move(instruction[0], int(instruction[1]), 1, head)
print(len(visited))
