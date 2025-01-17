# 입력이 얼마나 들어올지 모르는 상황에서 끝나는 시점의 조건도 없다면,
# try와 except를 사용해서 try로 시도하다가 오류가 나면, except로 빠져나오게 하면 된다.
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break