all_items = input().split("|")
budget = float(input())

new_items = []
total_profit = 0

for item in all_items:
    type_item, price_item = item.split("->")
    price_item = float(price_item)

    if type_item == "Clothes" and price_item > 50:
        continue
    elif type_item == "Shoes" and price_item > 35:
        continue
    elif type_item == "Accessories" and price_item > 20.50:
        continue

    if budget >= price_item:
        budget -= price_item
        profit = price_item * 0.40
        total_profit += profit
        new_items.append(price_item + profit)

for i in new_items:
    print(f"{i:.2f} ", end="")
print()
print(f"Profit: {total_profit:.2f}")

budget += sum(new_items)
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
