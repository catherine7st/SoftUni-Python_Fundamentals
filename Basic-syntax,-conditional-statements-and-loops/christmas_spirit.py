quantity = int(input())
days = int(input())

money = 0
spirit = 0

ornament = 2
skirt = 5
garlands = 3
lights = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        money += ornament * quantity
        spirit += 5
    if day % 3 == 0:
        money += (skirt * quantity + garlands * quantity)
        spirit += 13
    if day % 5 == 0:
        money += lights * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        money += (skirt + garlands + lights)
        if day == days:
            spirit -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")
