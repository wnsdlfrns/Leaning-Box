number = int(input())
count = 0

if number < 10:
  number *= 10

value = number

while True:
  count += 1
  a = value//10
  b = value%10
  x = a + b
  value = (b * 10) + (x % 10) 

  if value == number:
    break
    
print(count)