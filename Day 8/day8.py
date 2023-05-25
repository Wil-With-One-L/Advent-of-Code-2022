def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

lines = cleanInput("Day 8/input.txt")
grid = [] # grid[row][col]
for line in lines:
  row = []
  for c in line:
    row.append(int(c))
  grid.append(row)

max_score = 0
# iterate through each cell (ignore ones on the edges, they will have a score of 0)
for cell_y in range(1, len(grid) - 1):
  for cell_x in range(1, len(grid[cell_y]) - 1):
    # print('new')

    start_height = grid[cell_y][cell_x]
    # print(f"start_height: {start_height}")
    curr_score = 1

    # print(start_height)

    # right
    right = 0
    for col in range(cell_x + 1, len(grid[cell_y])):
      right += 1
      if grid[cell_y][col] >= start_height:
        break

    # print(right)
        
    # down
    down = 0
    for row in range(cell_y + 1, len(grid)):
      down += 1
      if grid[row][cell_x] >= start_height:
        break

    # print(down)

    # left
    left = 0
    for col in range(cell_x - 1, -1, -1):
      left += 1
      if grid[cell_y][col] >= start_height:
        break
    
    # print(left)

    # up
    up = 0
    for row in range(cell_y - 1, -1, -1):
      up += 1
      if grid[row][cell_x] >= start_height:
        break
    
    # print(up)

    curr_score = right * down * left * up
    # print(curr_score)

    max_score = max(max_score, curr_score)
  
print(max_score)
