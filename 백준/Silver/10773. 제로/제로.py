import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
  num = int(sys.stdin.readline())
  if num == 0:
    l.pop()
  else:
    l.append(num)

print(sum(l))
