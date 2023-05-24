def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n').split(',')
    for j in range(0, 2):
      lines[i][j] = lines[i][j].split('-')
  return lines

lines = cleanInput("Day 4/input.txt")

count = 0
for line in lines:
  start1 = int(line[0][0])
  end1 = int(line[0][1])
  start2 = int(line[1][0])
  end2 = int(line[1][1])

  if start2 >= start1 and start2 <= end1:
    count += 1
  elif start1 >= start2 and start1 <= end2:
    count += 1

print(count)