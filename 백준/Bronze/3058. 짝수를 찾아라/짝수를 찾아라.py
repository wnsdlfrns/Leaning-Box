n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    f = []
    for x in l:
        if x%2==0:
            f.append(x)
    print(sum(f), min(f))