nums_str = input()
cnt_nums = int(input())
biggest_nums = []

while cnt_nums > 0:
    sorted(nums_str)
    for number in nums_str:
        biggest_nums.append(number)
        cnt_nums -= 1

print(biggest_nums)
