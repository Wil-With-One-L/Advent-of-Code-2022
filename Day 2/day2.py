def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

# 0 is loss, 6 is win, 3 is draw

rounds = cleanInput("Day 2/input.txt")

A = dict() # rock
B = dict() # paper
C = dict() # scissors

A['X'] = 0 + 3
A['Y'] = 3 + 1
A['Z'] = 6 + 2

B['X'] = 0 + 1
B['Y'] = 3 + 2
B['Z'] = 6 + 3

C['X'] = 0 + 2
C['Y'] = 3 + 3
C['Z'] = 6 + 1

# points = dict()

# points['X'] = 1
# points['Y'] = 2
# points['Z'] = 3

total = 0
for round in rounds:
  sum = 0
  opp = round[0]
  resp = round[2]
  if opp == 'A':
    sum += A[resp]
  elif opp == 'B':
    sum += B[resp]
  elif opp == 'C':
    sum += C[resp]
  total += sum

print(total)
