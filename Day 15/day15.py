def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  pairs = []
  for i in range(0,len(lines)):
    lines[i] = lines[i].strip('\n').split(' ')
    lines[i].pop(0)
    lines[i].pop(0)
    lines[i].pop(2)
    lines[i].pop(2)
    lines[i].pop(2)
    lines[i].pop(2)
    for j in range(0, len(lines[i])):
      lines[i][j] = lines[i][j][2:].strip(',:')
    pair1 = (int(lines[i][0]), int(lines[i][1]))
    pair2 = (int(lines[i][2]), int(lines[i][3]))
    pairs.append((pair1, pair2))
  return pairs

def getBeaconLocations(pairs):
  beacons = []
  for pair in pairs:
    beacons.append(pair[1])
  return beacons

def getSensorLocations(pairs):
  sensors = []
  for pair in pairs:
    sensors.append(pair[0])
  return sensors

def getSensorBorder(pos, max_dist):
  x = pos[0]
  y = pos[1]
  cells = set()
  dist = max_dist + 1
  curr_y = y
  while dist >= 0:
    cells.add((x - dist, curr_y))
    cells.add((x + dist, curr_y))
    opp_y = (y - curr_y) + y
    cells.add((x - dist, opp_y))
    cells.add((x + dist, opp_y))
    curr_y -= 1
    dist -= 1
  return cells

def manhattan(p1, p2):
  x_dist = abs(p1[0] - p2[0])
  y_dist = abs(p1[1] - p2[1])
  return x_dist + y_dist

def getManDists(sensors, beacons):
  d = dict()
  for i in range(0, len(sensors)):
    d[sensors[i]] = manhattan(sensors[i], beacons[i]) 
  return d


# =========================

pairs = cleanInput('Day 15/input.txt')

# =========================

sensors = getSensorLocations(pairs)
beacons = getBeaconLocations(pairs)

# =========================

man_dists = getManDists(sensors, beacons)

# =========================

border_cells = set()
search_dist = 4000000

for pair in pairs:
  print(pair)
  sensor = pair[0]
  beacon = pair[1]
  border_cells = getSensorBorder(sensor, manhattan(sensor, beacon))
  for cell in border_cells:
    x = cell[0]
    y = cell[1]
    inside = False
    for sensor in sensors:
      # check if sensor's distance to cell is smaller than the sensor's max distance
      if manhattan(sensor, cell) <= man_dists[sensor]:
        inside = True
    if not inside:
      if cell[0] >= 0 and cell[0] <= search_dist:
        if cell[1] >= 0 and cell[1] <= search_dist:
          print("YOOO", cell, (x * 4000000) + y)
          exit()

# =========================
# make it pretty

# grid = []
# for y in range(-2, 23):
#   if y < 10 and y >= 0:
#     row = f'{y}  '
#   else:
#     row = f'{y} '
#   for x in range(-2, 26):
#     if (x,y) == (14, 11):
#       row += 'O'
#     elif (x, y) in border_cells:
#       row += '#'
#     else:
#       row += '.'
  
#   grid.append(row)

# for row in grid:
#   print(row)

# =========================
  



