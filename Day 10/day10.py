def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n').split(' ')
  return lines

def checkCycle(cycle, register):
  if cycle in [20, 60, 100, 140, 180, 220]:
    return cycle * register
  return 0

lines = cleanInput('Day 10/input.txt')

sum = 0
register = 1
cycle = 0

for line in lines:
  if line[0] == 'noop':
    cycle += 1
    sum += checkCycle(cycle, register)
  elif line[0] == 'addx':
    cycle += 1
    sum += checkCycle(cycle, register)
    cycle += 1
    sum += checkCycle(cycle, register)
    register += int(line[1])

# 14360 too high
# 13320 too low

print(sum)