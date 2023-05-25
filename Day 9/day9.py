def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n').split(' ')
  return lines

def isAdjacent(pos1, pos2):
  adjacents = [(0,0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
  diff = (pos1[0] - pos2[0], pos1[1] - pos2[1])
  if diff in adjacents:
    return True
  return False

def move(pos, dir):
  match dir:
    case 'R':
      return (pos[0] + 1, pos[1])
    case 'D':
      return (pos[0], pos[1] - 1)
    case 'L':
      return (pos[0] - 1, pos[1])
    case 'U':
      return (pos[0], pos[1] + 1)

def follow(head_pos, tail_pos, dir):
  if isAdjacent(head_pos, tail_pos):
    return tail_pos
  else:
    if dir == 'U':
      # if tail is in a different x coordinate than head:
      if head_pos[0] != tail_pos[0]:
        shift = head_pos[0] - tail_pos[0]
        return (tail_pos[0] + shift, tail_pos[1] + 1)
    elif dir == 'D':
      if head_pos[0] != tail_pos[0]:
        shift = head_pos[0] - tail_pos[0]
        return (tail_pos[0] + shift, tail_pos[1] - 1)
    elif dir == 'R':
      if head_pos[1] != tail_pos[1]:
        shift = head_pos[1] - tail_pos[1]
        return (tail_pos[0] + 1, tail_pos[1] + shift)
    elif dir == 'L':
      if head_pos[1] != tail_pos[1]:
        shift = head_pos[1] - tail_pos[1]
        return (tail_pos[0] - 1, tail_pos[1] + shift)
    return move(tail_pos, dir)

commands = cleanInput("Day 9/input.txt")

head_pos = (0,0)
tail_pos = (0,0)

visited = set() 
visited.add((0,0))

for command in commands:
  dir = command[0]
  steps = int(command[1])
  for i in range(0, steps):
    head_pos = move(head_pos, dir)
    tail_pos = follow(head_pos, tail_pos, dir)
    print(dir, tail_pos)
    visited.add(tail_pos)

# 6226 too high

print(visited)
print(len(visited))