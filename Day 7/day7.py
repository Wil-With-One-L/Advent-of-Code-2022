class File:
  def __init__(self, size):
    self.size = size

class Directory:
  def __init__(self, name, parent, files, directories):
    self.name = name
    self.parent = parent
    self.files = []
    self.directories = []
    self.size = 0

    for f in files:
      self.addFile(f)
    for d in directories:
      self.addDirectory(d)
  
  def addFile(self, file):
    self.files.append(file)
    self.size += file.size
  
  def addDirectory(self, directory):
    self.directories.append(directory)
    for f in directory.files:
      self.size += f.size
    for d in directory.directories:
      self.size += d.size

def cleanInput(filename):
  file = open(filename)
  lines = file.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')
  return lines

def search(directory):
  sizes = []
  sizes.append(directory.size)
  for d in directory.directories:
    sizes.extend(search(d))
  return sizes

# f1 = File(1)
# f2 = File(2)
# f3 = File(4)

# d1 = Directory('d1',[],[])
# d2 = Directory('d2',[],[])

# d1.addFile(f1)
# d1.addFile(f2)

# d2.addFile(f3)

# d1.addDirectory(d2)

# print(d1.size)
# print(d2.size)

directory_dict = dict()
directory_dict['root'] = Directory('root', 'None', [],[])

lines = cleanInput("Day 7/input.txt")

curr_dir = 'root'
ls_mode = False

for line in lines:
  print(line)
  line = line.split(' ')
  if line[0] == '$': # command
    ls_mode = False
    if line[1] == 'cd':
      if line[2] == '..':
        curr_dir = directory_dict[curr_dir].parent
      else:
        parent = curr_dir
        curr_dir = line[2]
        directory_dict[curr_dir] = Directory(curr_dir, parent, [], [])
    elif line[1] == 'ls':
      pass
  elif line[0] == 'dir': # dir 
    direc = Directory(line[1], curr_dir, [], [])
    directory_dict[curr_dir].addDirectory(direc)
  else: # file
    file = File(int(line[0]))
    directory_dict[curr_dir].addFile(file)
    
sizes = search(directory_dict['root'])
print(f"sizes: {sizes}")
print(directory_dict['root'].size)