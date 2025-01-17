N, B = input().split()
N = N[::-1]

list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i, c in enumerate(N):
    result += list.find(c) * (int(B)**i)

print(result)