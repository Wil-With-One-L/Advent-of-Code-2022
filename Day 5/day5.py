class StackSet:
  def __init__(self, stacks):
    self.stacks = stacks
    
  def move(self, number, source, dest):
    for i in range(0, number):
      box = self.stacks[source - 1].pop()
      self.stacks[dest - 1].append(box)


def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  
  for i in range(10, len(lines)):
    lines[i] = lines[i].strip('\n').split(' ')
  return lines[10:]

lines = cleanInput("Day 5/input.txt")

stack1 = ['R', 'G', 'J', 'B', 'T', 'V', 'Z']
stack2 = ['J', 'R', 'V', 'L']
stack3 = ['S', 'Q', 'F']
stack4 = ['Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G']
stack5 = ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W']
stack6 = ['S', 'W', 'T', 'C', 'H', 'F']
stack7 = ['D', 'Z', 'C', 'V', 'F', 'N', 'J']
stack8 = ['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q']
stack9 = ['J', 'B', 'W', 'V', 'P']

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

stack_set = StackSet(stacks)

for line in lines:
  number = int(line[1])
  source = int(line[3])
  dest = int(line[5])
  stack_set.move(number, source, dest)
  print(f"moved {number} from {source} to {dest}")
  # print(stack_set.stacks[5])

for stack in stack_set.stacks:
  print(stack[-1])