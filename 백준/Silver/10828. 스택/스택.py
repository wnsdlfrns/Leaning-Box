import sys
    
command = sys.stdin.readline
n = int(command().rstrip())
stack = []

for _ in range(n):
  x, *args = command().split()
  
  if x == 'push':
    stack.append(args[0])
    
  elif x == 'pop':
    print(f'{stack.pop() if stack else -1}')
  
  elif x == 'size':
    print(f'{len(stack)}')
    
  elif x == 'empty':
    print(f'{1 if not stack else 0}')
    
  elif x == 'top':
    print(f'{stack[-1] if stack else -1}')