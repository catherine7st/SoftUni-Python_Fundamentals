# numbers = input().split(", ")
# beggars = int(input())
#
# result = []
#
# for i in range(beggars):
#     result.append(0)
# i = 0
# while len(list_nums) > 0:
#     list_nums[0] = int(list_nums[0])
#     if i < len(result):
#         result[i] += list_nums[0]
#     else:
#         i = 0
#         continue
#     list_nums.pop(0)
#     i += 1
#
# print(result)
#
nums_str = input().split(",")
count = int(input())
nums = []

for num in nums_str:
    nums.append(int(num))

result_sum = [0] * count

for i in range(len(nums)):
    index = i % count
    result_sum[index] += nums[i]

print(result_sum)
