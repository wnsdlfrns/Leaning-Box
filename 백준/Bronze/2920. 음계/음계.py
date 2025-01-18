imp = list(map(int, input().split()))

if imp == sorted(imp):
    print('ascending')
elif imp == sorted(imp, reverse=True):
    print('descending')
else:
    print('mixed')