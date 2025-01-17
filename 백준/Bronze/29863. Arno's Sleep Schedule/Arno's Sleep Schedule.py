sleep = int(input())
wake = int(input())

if wake >= sleep:
    print(wake - sleep)
else:
    print(24 - sleep + wake)