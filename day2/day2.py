import re
inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day2/input.txt"
input = open(inputpath, "r")
fixed = [i.split() for i in input.read().split("\n")]


def part_one():
    score = 0
    """
    A = rock
    B = Paper
    C = Scissors
    X = Rock
    Y = Paper
    Z = Scissors
    0 = lost
    3 = draw
    6 = won
    """
    scoring = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    win = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
    draw = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }
    for game in fixed:
        score += 6 if win.get(game[0]) == game[1] else 0
        score += 3 if draw.get(game[0]) == game[1] else 0
        score += scoring.get(game[1])
    return score


def part_two():
    score = 0
    """
    A = rock
    B = Paper
    C = Scissors
    X = Lose
    Y = Draw
    Z = Win
    0 = lost
    3 = draw
    6 = won
    1 = Rock
    2 = Paper
    3 = Scissors
    """
    win = {
        'A': 8,
        'B': 9,
        'C': 7
    }
    draw = {
        'A': 4,
        'B': 5,
        'C': 6
    }
    lose = {
        'A': 3,
        'B': 1,
        'C': 2
    }
    scoring = {
        'X': lose,
        'Y': draw,
        'Z': win
    }
    for game in fixed:
        score += scoring.get(game[1]).get(game[0])
    return score


print(part_one())
print(part_two())
