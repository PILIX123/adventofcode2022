import re


inputpath = "/Users/pierr/Desktop/Funny/adventofcode2022/day7/input.txt"
commands = open(inputpath, "r").read().splitlines()
"""
var current dir
list available dir
list available files
find("\$ cd ").regs[0]
"""
directory = []
filesizes = {}
for command in commands:
    if command.startswith("$ cd"):
        if ".." in command:
            directory.pop(-1)
        else:
            directory.append(command.removeprefix("$ cd "))
            if ''.join(directory) not in filesizes.keys():
                filesizes.update({''.join(directory): 0})
        continue
    if (size := re.findall("\d+ ", command)) != []:
        updateall = []
        for folder in directory:
            updateall.append(folder)
            filesizes.update({''.join(updateall): filesizes.get(
                ''.join(updateall))+int(size[0])})
list_of_ = []
for keys in filesizes.keys():
    if filesizes.get(keys) <= 100000:
        list_of_.append(filesizes.get(keys))
print(sum(list_of_))
