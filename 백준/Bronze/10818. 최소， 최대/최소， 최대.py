import sys

_ = input()
numbers = list(map(int, sys.stdin.readline().replace('\n','').split()))
numbers.sort()
print(numbers[0], numbers[-1], sep=' ')