def total_order_price(string, num):
    if string == 'coffee':
        return num * 1.50
    elif string == 'water':
        return num * 1.00
    elif string == 'coke':
        return num * 1.40
    elif string == 'snacks':
        return num * 2.00


order = input()
quantity = int(input())

print(f"{total_order_price(order, quantity):.2f}")

