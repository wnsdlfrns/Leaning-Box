H, M = map(int, input().split())
wait_M = int(input())

# total_M = _H + _M + wait_M
# H, M = total_M//60, total_M%60

H += wait_M//60
M += wait_M%60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
    
print(f'{H} {M}')