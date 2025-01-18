import sys

lines = list(sys.stdin.read().split('\n'))
for i in range(30):
    i += 1
    if str(i) not in lines:
        print(i)