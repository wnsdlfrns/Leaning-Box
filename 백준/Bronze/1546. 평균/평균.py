input()
scores = list(map(int, input().split()))
max_score = max(scores)
fianl = 0

for i in scores:
    fianl += (i/max_score) * 100
    
print(fianl/len(scores))