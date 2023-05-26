import string

def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

def makeAlphaDict():
  d = dict()
  chars = list(string.ascii_lowercase)
  i = 0
  for c in chars:
    d[c] = i
    i += 1
  
  d['S'] = 0
  d['E'] = 26

  return d

def makeGrid(lines, alpha):
  grid = []
  for line in lines:
    row = []
    for c in line:
      row.append(alpha[c])
    # print(row)
    grid.append(row)
  return grid


lines = cleanInput('Day 12/input.txt')
alpha = makeAlphaDict()
elev_grid = makeGrid(lines, alpha)
# print(elev_grid)

start = (20, 0)
end = (20, 58)

distance = dict()

queue = []
visited = []

queue.append(start)
distance[start] = 0

# BFS
while len(queue) > 0:
  # get next non-visited cell
  while queue[0] in visited:
    queue.pop(0)
    if len(queue) == 0:
      break
  if len(queue) == 0:
    break

  curr = queue[0]
  row = curr[0]
  col = curr[1]
  elev = elev_grid[row][col]

  # add its traversable neighbors to queue
  # right
  if col < len(elev_grid[row]) - 1:
    if elev_grid[row][col + 1] <= elev + 1:
      cell = (row, col + 1)
      if cell in distance:
        distance[cell] = min(distance[curr] + 1, distance[cell])
      else:
        distance[cell] = distance[curr] + 1
      queue.append(cell)
  
  # down
  if row < len(elev_grid) - 1:
    if elev_grid[row + 1][col] <= elev + 1:
      cell = (row + 1, col)
      if cell in distance:
        distance[cell] = min(distance[curr] + 1, distance[cell])
      else:
        distance[cell] = distance[curr] + 1
      queue.append(cell)
  
  # left
  if col > 0:
    if elev_grid[row][col - 1] <= elev + 1:
      cell = (row, col - 1)
      if cell in distance:
        distance[cell] = min(distance[curr] + 1, distance[cell])
      else:
        distance[cell] = distance[curr] + 1
      queue.append(cell)

  # up
  if row > 0:
    if elev_grid[row - 1][col] <= elev + 1:
      cell = (row - 1, col)
      if cell in distance:
        distance[cell] = min(distance[curr] + 1, distance[cell])
      else:
        distance[cell] = distance[curr] + 1
      queue.append(cell)

  # give its neighbors a "distance" from start

  # (at the end) add cell to visited 
  visited.append(curr)
  queue.pop(0)

output = []
for row in range(0, 41):
  output_row = []
  for col in range(0, 81):
    if elev_grid[row][col] < 10:
      output_row.append('0' + str(elev_grid[row][col]) + ' ')
    else:
      output_row.append(str(elev_grid[row][col]) + ' ')
  output.append(output_row)

file = open('Day 12/output.txt', 'w')
for row in range(0, 41):
  file_row = ''
  for col in range(0, 81):
    file_row += output[row][col]
  file.write(file_row + '\n')

# make it pretty ===================
import cv2
import numpy as np
img = np.zeros((40,80,3), np.uint8)

# print(img.shape)
# blank_image[:,0:81//2] = (255,0,0)      # (B, G, R)
# blank_image[:,81//2:81] = (0,255,0)

# big = 360
# for y in range(0, 40):
#   for x in range(0, 80):
#     if distance.__contains__((y, x)):
#       color = distance[(y,x)] / big * 255
#     img[y,x] = (color, color, color) 
big = 27
for y in range(0, 40):
  for x in range(0, 80):
    color = elev_grid[y][x] / big * 255
    img[y,x] = (color, color, color) 
# ===================================

curr = end
commands = []
path = [(curr)]

print(distance[end])

while curr != start:
  # print(curr)

  row = curr[0]
  col = curr[1]

  right = -1
  down = -1
  left = -1
  up = -1

  # find the neighbor with distance(curr[0], curr[1]) - 1
  if col < len(elev_grid[row]) - 1:
    right = distance[(row, col + 1)]
  if row < len(elev_grid) - 1:
    down = distance[(row + 1, col)]
  if col > 0:
    left = distance[(row, col - 1)]
  if row > 0:
    up = distance[(row - 1, col)]
  
  if right == distance[curr] - 1:
    # print("yes")
    curr = (row, col + 1)
    commands.append('<')
  elif down == distance[curr] - 1:
    curr = (row + 1, col)
    commands.append('^')
  elif left == distance[curr] - 1:
    curr = (row, col - 1)
    commands.append('>')
  elif up == distance[curr] - 1:
    curr = (row - 1, col)
    commands.append('V')
    
  path.append(curr)

commands.reverse()
# print(commands)

img2 = img.copy()
for p in path:
  img2[p[0],p[1]] = (0,0,255)

cv2.imwrite("Day 12/img.png", img)
cv2.imwrite("Day 12/img2.png", img2)

# 352 too high
# 351 too high