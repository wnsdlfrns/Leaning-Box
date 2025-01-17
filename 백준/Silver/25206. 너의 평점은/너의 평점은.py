total_ave_grade = 0
total_grade = 0

rating = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}

for _ in range(20):
    _, average_score, my_score = map(str, input().split())
    average_score = float(average_score)
    if my_score != 'P':
        total_ave_grade += average_score
        total_grade += rating.get(my_score) * average_score

print(f'{total_grade/total_ave_grade:.6f}')
