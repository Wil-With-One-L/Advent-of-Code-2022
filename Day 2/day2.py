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

A['X'] = 3
A['Y'] = 6
A['Z'] = 0

B['X'] = 0
B['Y'] = 3
B['Z'] = 6

C['X'] = 6
C['Y'] = 0
C['Z'] = 3

points = dict()

points['X'] = 1
points['Y'] = 2
points['Z'] = 3

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
  total += sum + points[resp]

print(total)
