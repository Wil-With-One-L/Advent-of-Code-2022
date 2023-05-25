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

def follow(front, back):
  if isAdjacent(front, back):
    return back
  else:
    # if different y value
    if front[0] == back[0] and front[1] != back[1]:
      if front[1] > back[1]:
        return move(back, 'U')
      else:
        return move(back, 'D')
    # if different x value
    elif front[0] != back[0] and front[1] == back[1]:
      if front[0] > back[0]:
        return move(back, 'R')
      else:
        return move(back, 'L')
    
    # diagonal
    else:
      # Up Right
      if front[0] > back[0] and front[1] > back[1]:
        ret = move(back, 'U')
        return move(ret, 'R')
      # Up Left
      elif front[0] < back[0] and front[1] > back[1]:
        ret = move(back, 'U')
        return move(ret, 'L')
      # Down Right
      elif front[0] > back[0] and front[1] < back[1]:
        ret = move(back, 'D')
        return move(ret, 'R')
      # Down Left
      elif front[0] < back[0] and front[1] < back[1]:
        ret = move(back, 'D')
        return move(ret, 'L')

commands = cleanInput("Day 9/input.txt")

head_pos = (0,0)

neck1 = (0,0)
neck2 = (0,0)
neck3 = (0,0)
neck4 = (0,0)
neck5 = (0,0)
neck6 = (0,0)
neck7 = (0,0)
neck8 = (0,0)

tail_pos = (0,0)

visited = set() 
visited.add((0,0))

for command in commands:
  dir = command[0]
  steps = int(command[1])
  for i in range(0, steps):
    head_pos = move(head_pos, dir)
    neck1 = follow(head_pos, neck1)
    neck2 = follow(neck1, neck2)
    neck3 = follow(neck2, neck3)
    neck4 = follow(neck3, neck4)
    neck5 = follow(neck4, neck5)
    neck6 = follow(neck5, neck6)
    neck7 = follow(neck6, neck7)
    neck8 = follow(neck7, neck8)
    tail_pos = follow(neck8, tail_pos)
    # print(dir, tail_pos)
    visited.add(tail_pos)

# 1793 too low

# print(visited)
print(len(visited))