def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n').split(' ')
    lines[i][0] = lines[i][0].strip(':')
  return lines

# def get(d, key):
#   if key in d:
#     return d[key]
  


def makeDict(lines):
  d = dict()
  for line in lines:
    if len(line) == 2:
      d[line[0]] = int(line[1])
      # print(d[line[0]])

  while len(d) < len(lines):
    for line in lines:
      if len(line) == 4:
        thing1 = line[1]
        thing2 = line[3]
        operation = line[2]
        if operation == '+':
          if thing1 in d and thing2 in d:
            d[line[0]] = d[thing1] + d[thing2]
        elif operation == '-':
          if thing1 in d and thing2 in d:
            d[line[0]] = d[thing1] - d[thing2]
        elif operation == '*':
          if thing1 in d and thing2 in d:
            d[line[0]] = d[thing1] * d[thing2]
        elif operation == '/':
          if thing1 in d and thing2 in d:
            d[line[0]] = d[thing1] / d[thing2]
  return d

lines = cleanInput('Day 21/input.txt')

root_idx = 1534
humn_idx = 1602
i = 3592056845000

# root_idx = 0
# humn_idx = 7
# i = 0

while True:
  d = makeDict(lines)
  root_line = lines[root_idx]
  lines[humn_idx][1] = i

  if d[root_line[1]] == d[root_line[3]]:
    print('===========')
    print(i)
    print(d[root_line[1]], d[root_line[3]])
    print(d[root_line[1]] - d[root_line[3]])
    break
  
  print('===========')
  print(i)
  print(d[root_line[1]], d[root_line[3]])
  print(d[root_line[1]] - d[root_line[3]])

  d.clear()

  i += 1

# 3592056845087 too high