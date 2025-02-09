import sys
    
command = sys.stdin.readline
n = int(command().rstrip())
stack = []

for _ in range(n):
  x, *args = command().split()
  
  if x == '1':
    stack.append(args[0])
    
  elif x == '2':
    print(f'{stack.pop() if stack else -1}')
  
  elif x == '3':
    print(f'{len(stack)}')
    
  elif x == '4':
    print(f'{1 if not stack else 0}')
    
  elif x == '5':
    print(f'{stack[-1] if stack else -1}')