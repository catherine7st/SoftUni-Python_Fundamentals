n = int(input())

for num in range(1, n + 1):
    result = 0
    str_num = str(num)
    for char in str_num:
        result += int(char)
    if result == 5 or result == 7 or result == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')

