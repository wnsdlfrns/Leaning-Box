for _ in range(int(input())):
    A, B = map(sorted,list(input().split()))
    print(['Impossible','Possible'][A == B])