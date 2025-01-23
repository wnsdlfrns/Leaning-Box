import sys

n, m = map(int, sys.stdin.readline().split())

matrix = []

for _ in range(n):
  matrix.append(list(map(int, sys.stdin.readline().split())))
  
for i in range(n):
  add_nums = list(map(int, sys.stdin.readline().split()))
  for j in range(m):
    matrix[i][j] += add_nums[j]
    
for row in matrix:
  print(*row)