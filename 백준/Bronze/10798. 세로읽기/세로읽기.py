import sys

lines = []
str = ''

for _ in range(5):
  lines.append(sys.stdin.readline().replace('\n',''))
  
longger = len(max(lines, key=len))

for midx, line in enumerate(lines):
  if longger > len(line):
    for _ in range(longger-len(line)):
      line += '+'
    lines[midx] = line

for i in range(longger):

  for j in range(len(lines)):
    # print(lines[j][i], j, i)
    str += lines[j][i]
    
print(str.replace('+',''))