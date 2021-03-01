# def handle_product(product, products_quantity_dict):
#     if product in products_quantity_dict:
#         quantity = products_quantity_dict[product]
#         print(f"We have {quantity} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")
#
#
# def extract_products_quantity(products_quantity_str):
#     values = products_quantity_str.split(' ')
#     n = len(values)
#     return {values[i]: int(values[i+1]) for i in range(0, n, 2)}
#
#
# def solve(products_quantity_str, products_str):
#     products_quantities_dict = extract_products_quantity(products_quantity_str)
#     [handle_product(product, products_quantities_dict) for product in products_str.split(' ')]
#
#
# solve(input(), input())

data = input().split()

products = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products[key] = value

products_to_search = input().split()

for product in products_to_search:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
