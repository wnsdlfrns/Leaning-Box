import sys
n = int(input())
for _ in range(n):
    score = 0
    add = 1
    line = sys.stdin.readline().replace('\n','')
    for x in line:
        if x == 'O':
            score += 1 * add
            add += 1
        else:
            add = 1
    print(score)