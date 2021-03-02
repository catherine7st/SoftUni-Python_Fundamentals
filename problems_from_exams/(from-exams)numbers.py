list_numbers = list(map(int, input().split()))

average = sum(list_numbers) / len(list_numbers)

new_list = [num for num in list_numbers if num > average]
new_list.sort(reverse=True)

if len(new_list) == 0:
    print("No")
else:
    new_list = new_list[:5]
    print(*new_list)
