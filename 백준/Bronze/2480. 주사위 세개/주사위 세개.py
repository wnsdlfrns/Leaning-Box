A, B, C = map(int, input().split())
sorted = [A, B, C]

if A == B == C:
    print(10000+A*1000)

elif A == B or A == C:
    print(1000+A*100)

elif B == C:
    sorted.sort(reverse=True)
    print(1000+B*100)

else:
    sorted.sort(reverse=True)
    print(sorted[0]*100)