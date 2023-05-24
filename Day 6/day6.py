def cleanInput(filename):
  file = open(filename)
  line = file.read()
  return line

data = cleanInput("Day 6/input.txt")

recent = data[0:14]

for i in range(14, len(data)):
  recent = recent[1:]
  recent += data[i]

  recent_set = set(recent)
  if len(recent_set) == 14:
    print(i + 1)
    break

print(recent)