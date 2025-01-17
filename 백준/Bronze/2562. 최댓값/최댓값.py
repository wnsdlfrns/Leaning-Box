listed = []

for _ in range(9):
    listed.append(int(input()))

print(max(listed), listed.index(max(listed))+1, sep='\n')