# 반복문을 통해서 'input()'으로 여러줄을 입력 받는다면, 시간초과가 발생할 수 있다.
# 이유: 파라미터를 프롬프트에 띄우는 역할을 하기때문에 아무 인자를 넘겨주지 않아도 추가적인 부하를 가짐
# sys.stdin.readline() = stdin(표준입력), readline(줄별로 읽어옴)
# → 기능은 input()과 같지만, 부하가 적다.
import sys
n = int(input())
for _ in range(n):
    # a, b = map(int, input().split())
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)