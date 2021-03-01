# def solve(bakery_str):
#     values = bakery_str.split(' ')
#     bakery = {}
#     n = len(values)
#     bakery = {values[i]: int(values[i + 1]) for i in range(0, n, 2)}
#     print(bakery)
#
#
# solve(input())
#
# # for i in range(0, n, 2):
# #     food = values[i]
# #     quantity = int(values[i + 1])
# #     bakery[food] = quantity
#

data = input().split()

products = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products[key] = value

print(products)
