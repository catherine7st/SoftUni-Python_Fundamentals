nums = input().split()

nums.sort()
for num in reversed(nums):
    print(num, end="")
