def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

def makeBackpacks(lines):
  backpacks = []
  for line in lines:
    half = len(line) // 2
    backpack = (line[0:half], line[half:])
    backpacks.append(backpack)
  return backpacks

import string

def makePriorityDict():
  chars = list(string.ascii_letters)
  d = dict()
  i = 1
  for c in chars:
    d[c] = i
    i += 1
  return d

def findSharedItems(bp):
  comp1 = bp[0]
  comp2 = bp[1]
  shared = set()
  for item in comp1:
    if item in comp2:
      shared.add(item)
  return shared

backpacks = makeBackpacks(cleanInput("Day 3 /input.txt"))
priority = makePriorityDict()

total = 0
for bp in backpacks:
  shared = findSharedItems(bp)
  for item in shared:
    total += priority[item]
  

print(total)