def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n').split(' ')
    lines[i].pop(0)
    lines[i].pop(1)
    lines[i].pop(1)
    lines[i].pop(2)
    lines[i].pop(2)
    lines[i].pop(2)
    lines[i].pop(2)

    lines[i][1] = lines[i][1][5:].strip(';')
    for j in range(2, len(lines[i])):
      lines[i][j] =lines[i][j].strip(',')
  return lines

def makeFlow(lines):
  d = dict()
  for line in lines:
    valve = line[0]
    flow = int(line[1])
    d[valve] = flow
  return d

def makeAdj(lines):
  d = dict()
  for line in lines:
    valve = line[0]
    adjs = line[2:]
    d[valve] = adjs
  return d

def makeDistance(start, adj):
  dist = dict()
  dist[start] = 0

  visited = []
  queue = []

  queue.append(start)

  # BFS babyyyyyy
  while len(queue) > 0:
    # get next non-visited valve
    while queue[0] in visited:
      queue.pop(0)
      if len(queue) == 0:
        break
    if len(queue) == 0:
        break
    
    curr = queue[0]

    # add adj nodes to queue and give them (curr_dist + 1)
    for a in adj[curr]:
      queue.append(a)
      if a not in dist:
        dist[a] = dist[curr] + 1
      else:
        dist[a] = min(dist[curr] + 1, dist[a])
    
    visited.append(curr)
    queue.pop(0)

  return dist

def makeImprove(flow, dist, mins_left):
  improve = dict()
  for v in flow:
    improve[v] = flow[v] * (mins_left - (dist[v] + 1))
  return improve




# ==========================

lines = cleanInput('Day 16/test.txt')
# line[0] = valve
# line[1] = flow rate
# line[2:] = connecting valves

# ==========================

flow = makeFlow(lines)
adj = makeAdj(lines)
# print(flow)
# print(adj)

# =====================
open_valves = []

total_improvement = 0

mins_left = 30
start = lines[0][0]

while mins_left > 0:
  print('===============')
  distance = makeDistance(start, adj)
  best_improvement = 0
  imp = makeImprove(flow, distance, mins_left)

  print(imp)

  for v in imp:
    if imp[v] > best_improvement and mins_left > distance[v] and v not in open_valves:
      best_improvement = imp[v]
      start = v

  if start in open_valves:
    break
  
  open_valves.append(start)
  mins_left = mins_left - (distance[start] + 1)
  if mins_left > 0:
    total_improvement += best_improvement  

  print(open_valves)
  print(f'distance to best valve ({start}): {distance[start]}')
  print(f'mins left: {mins_left}')
  print(f'best_improvement: {best_improvement}')
  print(f'total_improvement: {total_improvement}')


  
print(total_improvement)

# 13740 too high
# 1200 too low