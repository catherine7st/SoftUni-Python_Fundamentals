str_1 = input()
str_2 = input()

now_str = ""
before_str = str_1

for iteration in range(len(str_1)):
    for index_str_2 in range(0, iteration + 1):
        now_str += str_2[index_str_2]
    for index_str_1 in range(iteration + 1, len(str_1)):
        now_str += str_1[index_str_1]
    if not before_str == now_str:
        print(now_str)

    before_str = now_str
    now_str = ""
