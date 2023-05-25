def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

lines = cleanInput("Day 8/input.txt")
grid = [] # grid[row][col]
seen = []
for line in lines:
  seen_row = []
  row = []
  for c in line:
    row.append(int(c))
    seen_row.append(0)
  grid.append(row)
  seen.append(seen_row)

# left -> right
for row in range(0, len(grid)):
  curr_highest = -1
  for col in range(0, len(grid[row])):
    if grid[row][col] > curr_highest:
      curr_highest = grid[row][col]
      seen[row][col] = 1

# top -> bottom
for col in range(0, len(grid[0])):
  curr_highest = -1
  for row in range(0, len(grid)):
    if grid[row][col] > curr_highest:
      curr_highest = grid[row][col]
      seen[row][col] = 1

# right -> left
for row in range(len(grid) - 1, -1, -1):
  curr_highest = -1
  for col in range(len(grid[row]) - 1, -1, -1):
    if grid[row][col] > curr_highest:
      curr_highest = grid[row][col]
      seen[row][col] = 1

# bottom -> top
for col in range(len(grid[row]) - 1, -1, -1):
  curr_highest = -1
  for row in range(len(grid) - 1, -1, -1):
    if grid[row][col] > curr_highest:
      curr_highest = grid[row][col]
      seen[row][col] = 1

count = 0
for row in seen:
  for n in row:
    if n == 1:
      count += 1
print(count)