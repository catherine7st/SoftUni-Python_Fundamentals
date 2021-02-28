string = input()

current_list = string.split(" ")
next_list = []

for num in current_list:
    next_list.append(int(num) * -1)

print(next_list)

# if int(num) < 0:
#     next_list.append(abs(int(num)))
# else:
#     next_list.append(-abs(int(num)))
