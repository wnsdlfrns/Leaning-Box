import sys

maximum = 0
x, y = 0, 0

for i in range(9):
  get = list(map(int, sys.stdin.readline().split()))
  for j in range(9):
    # if max(get) > maximum:
    #   maximum = max(get)
    if get[j] > maximum:
      maximum = get[j]
      x = i
      y = j
      
print(f'{maximum}\n{x+1} {y+1}')