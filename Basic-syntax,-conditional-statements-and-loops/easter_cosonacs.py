budget = float(input())
flour_price = float(input())

egg_price = flour_price * 75 / 100
milk_price = flour_price + (flour_price * 25 / 100)
milk_250ml = milk_price / 4
cozonak_price = flour_price + egg_price + milk_250ml
colored_eggs = 0
cnt_cozonac = 0
left_money = 0

while cozonak_price <= budget:
    cnt_cozonac += 1
    budget -= cozonak_price
    left_money = budget
    colored_eggs += 3

    if cnt_cozonac % 3 == 0:
        colored_eggs = colored_eggs - (cnt_cozonac - 2)

print(f"You made {cnt_cozonac} cozonacs! Now you have {colored_eggs} eggs and {left_money:.2f}BGN left.")
