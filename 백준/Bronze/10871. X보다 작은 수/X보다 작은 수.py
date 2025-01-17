n, x = map(int, input().split())
list = input().split()

for i in range(n):
    if int(list[i]) < x:
        print(list[i], end=' ')