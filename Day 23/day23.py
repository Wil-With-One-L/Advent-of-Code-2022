import copy

def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

def makeGrid(lines):
  grid = []
  for line in lines:
    row = []
    for c in line:
      row.append(c)
    grid.append(row)
  return grid

def getPositions(grid):
  positions = []
  for r in range(0, len(grid)):
    for c in range(0, len(grid[r])):
      if grid[r][c] == '#':
        positions.append((r, c))
  return positions

def makeMoveDeclarations(grid, elf_positions, shift):
  moves = dict()
  for pos in elf_positions:
    if checkAlone(grid, pos):
      continue
    # gross. maybe handle the shift better
    if shift == 0:
      if checkUp(grid, pos):
        moves[pos] = (pos[0] - 1, pos[1])
      elif checkDown(grid, pos):
        moves[pos] = (pos[0] + 1, pos[1])
      elif checkLeft(grid, pos):
        moves[pos] = (pos[0], pos[1] - 1)
      elif checkRight(grid, pos):
        moves[pos] = (pos[0], pos[1] + 1)
    elif shift == 1:
      if checkDown(grid, pos):
        moves[pos] = (pos[0] + 1, pos[1])
      elif checkLeft(grid, pos):
        moves[pos] = (pos[0], pos[1] - 1)
      elif checkRight(grid, pos):
        moves[pos] = (pos[0], pos[1] + 1)
      elif checkUp(grid, pos):
        moves[pos] = (pos[0] - 1, pos[1])
    elif shift == 2:
      if checkLeft(grid, pos):
        moves[pos] = (pos[0], pos[1] - 1)
      elif checkRight(grid, pos):
        moves[pos] = (pos[0], pos[1] + 1)
      elif checkUp(grid, pos):
        moves[pos] = (pos[0] - 1, pos[1])
      elif checkDown(grid, pos):
        moves[pos] = (pos[0] + 1, pos[1])
    elif shift == 3:
      if checkRight(grid, pos):
        moves[pos] = (pos[0], pos[1] + 1)
      elif checkUp(grid, pos):
        moves[pos] = (pos[0] - 1, pos[1])
      elif checkDown(grid, pos):
        moves[pos] = (pos[0] + 1, pos[1])
      elif checkLeft(grid, pos):
        moves[pos] = (pos[0], pos[1] - 1)
  
  return moves
    
def move(grid, moves):
  restrictions = makeRestritctions(moves)
  for move in moves:
    if moves[move] in restrictions:
      continue
    else:
      grid[move[0]][move[1]] = '.'
      grid[moves[move][0]][moves[move][1]] = '#'
  return grid

def makeRestritctions(moves):
  move_locations = []
  restrictions = []

  for move in moves:
    if moves[move] in restrictions:
      continue
    if moves[move] in move_locations:
      restrictions.append(moves[move])
      move_locations.remove(moves[move])
    else:
      move_locations.append(moves[move])

  return restrictions

def addSpace(grid, n):
  row_len = len(grid[0])

  for row in grid:
    for i in range(0, n):
      row.insert(0, '.')
      row.append('.')
    
  new_line = []
  for i in range(0, row_len + (2 * n)):
    new_line.append('.')

  for i in range(0, n):
    grid.insert(0, copy.deepcopy(new_line))
    grid.append(copy.deepcopy(new_line))

  return grid

# ========================

def checkN(grid, pos):
  if pos[0] == 0:
    return False
  
  if grid[pos[0] - 1][pos[1]] == '#':
    return False
  else:
    return True

def checkNE(grid, pos):
  if pos[0] == 0 or pos[1] == len(grid[pos[0]]) - 1:
    return False
  
  if grid[pos[0] - 1][pos[1] + 1] == '#':
    return False
  else:
    return True

def checkNW(grid, pos):
  if pos[0] == 0 or pos[1] == len(grid[pos[0]]) - 1:
    return False
  
  if grid[pos[0] - 1][pos[1] - 1] == '#':
    return False
  else:
    return True

def checkE(grid, pos):
  if pos[1] == len(grid[pos[0]]) - 1:
    return False
  
  if grid[pos[0]][pos[1] + 1] == '#':
    return False
  else:
    return True

def checkSE(grid, pos):
  if pos[0] == len(grid) - 1 or pos[1] == len(grid[pos[0]]) - 1:
    return False
  
  if grid[pos[0] + 1][pos[1] + 1] == '#':
    return False
  else:
    return True
  
def checkS(grid, pos):
  if pos[0] == len(grid) - 1:
    return False
  
  if grid[pos[0] + 1][pos[1]] == '#':
    return False
  else:
    return True

def checkSW(grid, pos):
  if pos[0] == len(grid) - 1 or pos[1] == 0:
    return False
  
  if grid[pos[0] + 1][pos[1] - 1] == '#':
    return False
  else:
    return True

def checkW(grid, pos):
  if pos[0] == len(grid) - 1 or pos[1] == 0:
    return False
  
  if grid[pos[0]][pos[1] - 1] == '#':
    return False
  else:
    return True

# ======================

def checkUp(grid, pos):
  return checkNW(grid, pos) and checkN(grid, pos) and checkNE(grid, pos)

def checkDown(grid, pos):
  return checkSW(grid, pos) and checkS(grid, pos) and checkSE(grid, pos)

def checkLeft(grid, pos):
  return checkNW(grid, pos) and checkW(grid, pos) and checkSW(grid, pos)

def checkRight(grid, pos):
  return checkNE(grid, pos) and checkE(grid, pos) and checkSE(grid, pos)

def checkAlone(grid, pos):
  row = pos[0]
  col = pos[1]

  if row != 0 and grid[row - 1][col] == '#':
    return False
  if row != 0 and col != 0 and grid[row - 1][col - 1] == '#':
    return False
  if row != 0 and col != len(grid[row]) - 1 and grid[row - 1][col + 1] == '#':
    return False
  if row != len(grid) - 1 and grid[row + 1][col] == "#":
    return False
  if row != len(grid) - 1 and col != 0 and grid[row + 1][col - 1] == "#":
    return False
  if row != len(grid) - 1 and col != len(grid[row]) - 1 and grid[row + 1][col + 1] == "#":
    return False
  if col != 0 and grid[row][col - 1] == '#':
    return False
  if col != len(grid[row]) - 1 and grid[row][col + 1] == '#':
    return False
  
  return True

# ======================

lines = cleanInput("Day 23/input.txt")

grid = makeGrid(lines)
grid = addSpace(grid, 40)

num_elves = len(getPositions(grid))

# for line in grid:
#   print(line)
# ======================

for i in range(0, 10):
  elf_positions = getPositions(grid)
  move_map = makeMoveDeclarations(grid, elf_positions, i % 4)
  grid = move(grid, move_map)

# ======================
# make it pretty
file = open("Day 23/output.txt", "w")

for line in grid:
  string = ''
  for c in line:
    string += c
  file.write(string + '\n')

# ======================
# find bounding box

top = 0
for i in range(0, len(grid)):
  if '#' in grid[i]:
    top = i
    break

bot = 0
for i in range(len(grid) - 1, -1, -1):
  if '#' in grid[i]:
    bot = i
    break

left = 0
for col in range(0, len(grid[0])):
  for row in range(0, len(grid)):
    if grid[row][col] == '#':
      left = col
      break
  if left != 0:
    break

right = 0
for col in range(len(grid[0]) - 1, -1, -1):
  for row in range(0, len(grid)):
    if grid[row][col] == '#':
      right = col
      break
  if right != 0:
    break

print(bot, top)
print(right, left)

height = bot - top
width = right - left
print(((height + 1) * (width + 1)) - num_elves)

# 3757 too low
# 3917 correct!