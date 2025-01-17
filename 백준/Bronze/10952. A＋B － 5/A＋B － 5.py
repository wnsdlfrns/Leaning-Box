a, b = 1, 1
while a+b:
    a, b = map(int, input().split())
    if a+b:
        print(a+b)