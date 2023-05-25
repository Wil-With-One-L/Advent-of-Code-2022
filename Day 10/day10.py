def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n').split(' ')
  return lines

def drawPixel(cycle, register):
  if cycle % 40 in [register - 1, register, register + 1]:
    return '#'
  return '.'

lines = cleanInput('Day 10/input.txt')

register = 3
cycle = 1

grid = []
row = ''

for line in lines:
  if line[0] == 'noop':
    cycle += 1
    row += drawPixel(cycle, register)
    if len(row) == 40:
      new_row = ''
      for c in row:
        new_row += c
      grid.append(new_row)
      row = ''
  elif line[0] == 'addx':
    cycle += 1
    row += drawPixel(cycle, register)
    if len(row) == 40:
      new_row = ''
      for c in row:
        new_row += c
      grid.append(new_row)
      row = ''
    cycle += 1
    row += drawPixel(cycle, register)
    if len(row) == 40:
      new_row = ''
      for c in row:
        new_row += c
      grid.append(new_row)
      row = ''
    register += int(line[1])

# 14360 too high
# 13320 too low

for row in grid:
  print(row)