def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

lines = cleanInput("Day 1/Puzzle 1/input.txt")

curr_sum = 0
max_sum = 0
for line in lines:
  if line == '':
    max_sum = max(curr_sum, max_sum)
    curr_sum = 0
    continue
  curr_sum += int(line)

print(max_sum)