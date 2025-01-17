N = int(input())

for a in range(N):
    print('@' * (N * 3) + ' ' * N + '@' * N)

for b in range(N*3):
    print('@' * N + ' ' * N + '@' * N + ' ' * N + '@' * N)
    
for c in range(N):
    print('@' * N + ' ' * N + '@' * (N * 3))