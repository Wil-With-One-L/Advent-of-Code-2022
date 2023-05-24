def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

# def makeBackpacks(lines):
#   backpacks = []
#   for line in lines:
#     half = len(line) // 2
#     backpack = (line[0:half], line[half:])
#     backpacks.append(backpack)
#   return backpacks

def makeGroups(lines):
  groups = []
  curr_group = []
  for i in range(1, len(lines) + 1):
    curr_group.append(lines[i - 1])
    if i % 3 == 0:
      groups.append(curr_group)
      curr_group = []
  return groups

import string

def makePriorityDict():
  chars = list(string.ascii_letters)
  d = dict()
  i = 1
  for c in chars:
    d[c] = i
    i += 1
  return d

def findSharedItem(group):
  for c in group[0]:
    if c in group[1] and c in group[2]:
      return c

priority = makePriorityDict()
groups = makeGroups(cleanInput("Day 3/input.txt"))

total = 0
for group in groups:
  total += priority[findSharedItem(group)]

print(total)

# total = 0
# for bp in backpacks:
#   shared = findSharedItems(bp)
#   for item in shared:
#     total += priority[item]
  
