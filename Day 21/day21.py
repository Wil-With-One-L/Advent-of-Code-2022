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
      print(d[line[0]])

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

d = makeDict(lines)

print(int(d['root']))
