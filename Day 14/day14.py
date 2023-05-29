def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n').split(' -> ')
  return lines

def getCells(start,end):
  cells = set()

  # print(end)

  if int(start[0]) < int(end[0]):
    for x in range(int(start[0]), int(end[0]) + 1):
      cells.add((x, int(start[1])))
  else:
    for x in range(int(start[0]), int(end[0]) - 1, -1):
      cells.add((x, int(start[1])))
  
  if int(start[1]) < int(end[1]):
    for y in range(int(start[1]), int(end[1]) + 1):
      cells.add((int(start[0]), y))
  else:
    for y in range(int(start[1]), int(end[1]) - 1, -1):
      cells.add((int(start[0]), y))
  print(cells)
  return cells

def makeStone(lines):
  stone = set()
  for line in lines:
    for i in range(0, len(line) - 1):
      start = line[i]
      end = line[i + 1]
      for cell in getCells(start, end):
        stone.add(cell)
  return stone

def makeGrid(stone):
  grid = []
  for r in range(0, 200):
    row = []
    for c in range(0, 1000):
      # if (c, r) == (500, 0):
      #   row.append('o')
      #   continue
      if (c, r) in stone:
        row.append('#')
      else:
        row.append('.')
    grid.append(row.copy())
  return grid



# ============================

lines = cleanInput('Day 14/input.txt')

for i in range(0, len(lines)):
  for j in range(len(lines[i])):
    lines[i][j] = lines[i][j].split(',')

# for line in lines:
#   print(line)

# ============================

stone = makeStone(lines)

# ============================

grid = makeGrid(stone)

for i in range(0, 1000):
  grid[162][i] = '#'

# ===========================

for i in range(0, 24589):
  # print(i)
  sand = (0, 500)
  
  while sand[0] < 165:
    y = sand[0]
    x = sand[1]

    if grid[y + 1][x] == '.':
      sand = (y + 1, x)
    elif grid[y + 1][x - 1] == '.':
      sand = (y + 1, x - 1)
    elif grid[y + 1][x + 1] == '.':
      sand = (y + 1, x + 1)
    else:
      # print(i)
      grid[y][x] = 'o'
      break
  
  if grid[0][500] == 'o':
    print(i)
    break

# ===========================

# sand = (0, 500)
# while sand[0] < 165:
#   y = sand[0]
#   x = sand[1]

#   if grid[y + 1][x] == '.':
#     sand = (y + 1, x)
#   elif grid[y + 1][x - 1] == '.':
#     sand = (y + 1, x - 1)
#   elif grid[y + 1][x + 1] == '.':
#     sand = (y + 1, x + 1)
#   grid[y][x] = 'X'

# ===========================

file = open('output.txt', 'w')

for row in grid:
  line = ''
  for col in row:
    line += col
  file.write(line + '\n')

# ===========================

# 24588 too low
# it was 24589 lol