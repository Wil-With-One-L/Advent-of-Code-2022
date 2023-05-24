def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

lines = cleanInput("Day 1/input.txt")

curr_sum = 0
first = 0
second = 0
third = 0
for line in lines:
  if line == '':
    if curr_sum >= first:
      third = second
      second = first
      first = curr_sum
    elif curr_sum >= second:
      third = second
      second = curr_sum
    elif curr_sum > third:
      third = curr_sum
    curr_sum = 0
    continue
  curr_sum += int(line)

print(first, second, third)
print(first + second + third)