RANGE_LOW = range(1, 51)
RANGE_MEDIUM = range(51, 81)
RANGE_HIGH = range(81, 126)

effort = 0
putout_fire = []

fire_data = input().split("#")
water = int(input())

for fire in fire_data:
    type_fire, value = fire.split(" = ")
    value = int(value)

    if type_fire == "High" and value not in RANGE_HIGH:
        continue
    elif type_fire == "Medium" and value not in RANGE_MEDIUM:
        continue
    elif type_fire == "Low" and value not in RANGE_LOW:
        continue

    if water >= value:
        water -= value
        effort += value * 0.25
        putout_fire.append(value)

print("Cells:")
for fire in putout_fire:
    print(f" - {fire}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(putout_fire)}")