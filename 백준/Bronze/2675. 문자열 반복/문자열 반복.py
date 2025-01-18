n = int(input())
for _ in range(n):
    each, words = input().split()
    for char in words:
        print(f'{char*int(each)}', end='')
    print()