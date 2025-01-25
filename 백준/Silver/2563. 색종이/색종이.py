import sys

n = int(input())
dohwaji = [ [0] * 100 for _ in range(100) ]
total_area = []

for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  
  for i in range(x, x+10):
    for j in range(y, y+10):
      dohwaji[i][j] = 1

total_area = [ sum(dohwaji[i]) for i in range(100) ]
total_area = sum(total_area)

print(total_area)

# print(dohwaji[i] for i in range(100), sep='\n')

# for i in range(100):
#   print(sum(dohwaji[i]))