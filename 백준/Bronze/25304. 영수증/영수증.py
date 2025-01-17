x, n = int(input()), int(input())

for _ in range(n):
    price, ea = map(int, input().split())
    x -= price * ea

if x:
    print('No')
else:
    print('Yes')