def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n').split(',')
    for j in range(0, 3):
      lines[i][j] = int(lines[i][j])
  return lines

def getNeighbors(cube, size):
  neighbors = []
  if cube[0] < size - 1:
    neighbors.append([cube[0] + 1, cube[1], cube[2]])
  if cube[0] > 0:
    neighbors.append([cube[0] - 1, cube[1], cube[2]])
  if cube[1] < size - 1:
    neighbors.append([cube[0], cube[1] + 1, cube[2]])
  if cube[1] > 0:
    neighbors.append([cube[0], cube[1] - 1, cube[2]])
  if cube[2] < size - 1:
    neighbors.append([cube[0], cube[1], cube[2] + 1])
  if cube[2] > 0:
    neighbors.append([cube[0], cube[1], cube[2] - 1])
  return neighbors

def getExterior(cubes, size):
  exteriors = []

  # BFS babEEEYYYYY
  start = [0,0,0]
  visited = []
  queue = []

  queue.append(start)
    
  while len(queue) > 0:
    # get next non-visited cell
    while queue[0] in visited:
      queue.pop(0)
      if len(queue) == 0:
        break
    if len(queue) == 0:
      break
  
    cube = queue[0]  
    
    # add all EMPTY neighbors to queue:
    neighbors = getNeighbors(cube, size)
    for n in neighbors:
      if (n not in cubes) and (n not in visited):
        queue.append(n)
  
    exteriors.append(cube)
    visited.append(cube)
    queue.pop(0)
  
  return exteriors

# =======================

size = 22
# grid = make3DGrid(grid_size)

# =======================

cubes = cleanInput('Day 18/input.txt')
# print(cubes)

# =======================

exterior_cubes = getExterior(cubes, size)

total = 0

for cube in cubes:
  neighbors = getNeighbors(cube, size)
  sides = 6
  for neighbor in neighbors:
    if neighbor in cubes or neighbor not in exterior_cubes:
      sides -= 1
  total += sides
      
print(total)

# 1905 too low
# 1958 too low

# 1996!