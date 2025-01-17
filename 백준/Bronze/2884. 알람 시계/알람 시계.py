H, M = map(int, input().split())

if 45 > M:
    if H == 0:
        H = 24
    H -= 1
    M += 60 - 45
else:
    M -= 45

print(f'{H} {M}')