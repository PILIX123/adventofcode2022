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

    def move(self, direction, movement, length, head: Head):
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


head = Head()
tail = Tail()
visit = {str((tail.x, tail.y)): "visited"}
visited.update(visit)
number = 1
for instruction in data:
    head.move(instruction[0], int(instruction[1]))
    tail.move(instruction[0], int(instruction[1]), 1, head)
    number += 1

print(len(visited))
