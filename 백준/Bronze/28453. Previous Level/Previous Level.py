n = int(input())
levels = input().split()

ranking = []

for i in range(n):
    your_step = int(levels[i])
    if your_step >= 300:
        ranking.append(1)
    elif your_step >= 275:
        ranking.append(2)
    elif your_step >= 250:
        ranking.append(3)
    else:
        ranking.append(4)

print(*ranking)