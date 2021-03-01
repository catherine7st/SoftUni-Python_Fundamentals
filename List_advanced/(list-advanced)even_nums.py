# nums = [int(el) for el in input().split(', ')]
# even_nums = [i for i in range(len(nums)) if nums[i] % 2 == 0]

nums = list(map(int, input().split(', ')))
even_nums = list(filter(lambda i: nums[i] % 2 == 0, range(len(nums))))

print(even_nums)
