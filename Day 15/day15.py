def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  pairs = []
  for i in range(0, len(lines)):
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


# =========================

pairs = cleanInput('Day 15/input.txt')

# =========================

beacons = getBeaconLocations(pairs)

# =========================

target = 2000000
impossibles = set() # set of x coords within row that cannot be 

for pair in pairs:
  sensor = pair[0]
  beacon = pair[1]
  x_dist = abs(sensor[0] - beacon[0])
  y_dist = abs(sensor[1] - beacon[1])
  max_dist = x_dist + y_dist

  y_dist_from_target = abs(target - sensor[1])
  # impossible_cells = abs(max_dist - y_dist_from_2mil)

  if y_dist_from_target > max_dist:
    # print('--------')
    # print('hit')
    continue

  num_to_add = ((max_dist - y_dist_from_target) * 2) + 1
  for i in range(sensor[0] - (max_dist - y_dist_from_target), sensor[0] + (max_dist - y_dist_from_target) + 1):
    if (i, target) not in beacons:
      impossibles.add(i)

  # print('--------')
  # print(x_dist, y_dist)
  # print(y_dist_from_target)
  # print(num_to_add)

# for p in pairs:
#   print(p)

# print(impossibles)
print(len(impossibles))