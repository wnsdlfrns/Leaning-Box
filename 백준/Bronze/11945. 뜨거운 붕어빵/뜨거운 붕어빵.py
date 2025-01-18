import sys

line = ''
H, _ = map(int, input().split())
for _ in range(H):
    line = list(map(str, sys.stdin.readline().replace('\n','')))
    line.reverse()
    print(*line, sep='')