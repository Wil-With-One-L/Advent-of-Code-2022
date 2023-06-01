def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n').split(',')
    for j in range(0, 3):
      lines[i][j] = int(lines[i][j])
  return lines

def getNeighbors(cube):
  neighbors = []
  neighbors.append([cube[0] + 1, cube[1], cube[2]])
  neighbors.append([cube[0] - 1, cube[1], cube[2]])
  neighbors.append([cube[0], cube[1] + 1, cube[2]])
  neighbors.append([cube[0], cube[1] - 1, cube[2]])
  neighbors.append([cube[0], cube[1], cube[2] + 1])
  neighbors.append([cube[0], cube[1], cube[2] - 1])
  return neighbors


# def make3DGrid(size):
#   grid = []
#   for x in range(0, size):
#     row = []
#     for y in range(0, size):
#       col = []
#       for z in range(0, size):
#         col.append(0)
#       row.append(col)
#     grid.append(row)
#   return grid

# =======================

grid_size = 19
# grid = make3DGrid(grid_size)

# =======================

cubes = cleanInput('Day 18/input.txt')
print(cubes)

total = 0

for cube in cubes:
  neighbors = getNeighbors(cube)
  sides = 6
  for neighbor in neighbors:
    if neighbor in cubes:
      sides -= 1
  total += sides
      
print(total)

# 3338 too high
# 3320 too low