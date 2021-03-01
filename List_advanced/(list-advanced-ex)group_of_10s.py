from math import ceil
all_numbers = input().split(", ")
nums = list(map(int, all_numbers))

for i in range(1, ceil(max(nums) / 10) + 1):
    result = [nums[j] for j in range(len(nums)) if nums[j] in range(i * 10 - 10 + 1, i * 10 + 1)]
    print(f"Group of {i*10}'s: {result}")
