nums = []
for _ in range(10):
    x = int(input())
    if x%42 not in nums:
        nums.append(x%42)
print(len(nums))