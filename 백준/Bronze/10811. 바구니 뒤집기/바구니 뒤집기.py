import sys

n, m = map(int, sys.stdin.readline().split())
list_data = list(range(1, n+1))

for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())
  list_data[x-1:y] = list_data[x-1:y][::-1]

print(*list_data)