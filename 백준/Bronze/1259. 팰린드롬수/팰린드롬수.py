import sys

while True:
  line = int(sys.stdin.readline())
  if line:
    line = str(line)
    
    if line[::1] == line[::-1]:
      print('yes')
      
    else:
      print('no')
    
    
  else:
    break