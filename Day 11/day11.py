items_d = dict()
ops_d = dict()
tests_d = dict()
true_d = dict()
false_d = dict()

# ======================

items_d[0] = [85, 79, 63, 72] 
ops_d[0] = lambda old : old * 17
tests_d[0] = lambda n : n % 2
true_d[0] = 2
false_d[0] = 6

items_d[1] = [53, 94, 65, 81, 93, 73, 57, 92] 
ops_d[1] = lambda old : old * old
tests_d[1] = lambda n : n % 7
true_d[1] = 0
false_d[1] = 2

items_d[2] = [62, 63]
ops_d[2] = lambda old : old + 7
tests_d[2] = lambda n : n % 13
true_d[2] = 7
false_d[2] = 6

items_d[3] = [57, 92, 56]
ops_d[3] = lambda old : old + 4
tests_d[3] = lambda n : n % 5
true_d[3] = 4
false_d[3] = 5

items_d[4] = [67]
ops_d[4] = lambda old : old + 5
tests_d[4] = lambda n : n % 3
true_d[4] = 1
false_d[4] = 5

items_d[5] = [85, 56, 66, 72, 57, 99]
ops_d[5] = lambda old : old + 6
tests_d[5] = lambda n : n % 19
true_d[5] = 1
false_d[5] = 0

items_d[6] = [86, 65, 98, 97, 69]
ops_d[6] = lambda old : old * 13
tests_d[6] = lambda n : n % 11
true_d[6] = 3
false_d[6] = 7

items_d[7] = [87, 68, 92, 66, 91, 50, 68]
ops_d[7] = lambda old : old + 2
tests_d[7] = lambda n : n % 17
true_d[7] = 4
false_d[7] = 3

# =====================

inspections = dict()
inspections[0] = 0
inspections[1] = 0
inspections[2] = 0
inspections[3] = 0
inspections[4] = 0
inspections[5] = 0
inspections[6] = 0
inspections[7] = 0

rounds = 20
for r in range(0, rounds):
  for monkey in range(0, 8):
    inspect_count = 0
    for i in items_d[monkey]:
      inspect_count += 1
      i = ops_d[monkey](i)
      i //= 3
      if tests_d[monkey](i) == 0:
        items_d[true_d[monkey]].append(i)
      else:
        items_d[false_d[monkey]].append(i)
    items_d[monkey].clear()
    inspections[monkey] += inspect_count

first = 0
second = 0
for i in range(0, 8):
  if inspections[i] > first:
    second = first
    first = inspections[i]
  elif inspections[i] > second:
    second = inspections[i]

print(first, second)
print(first * second)

# 3376659201294824640 too high