n_lines = int(input())

capacity = 255
cnt_liters = 0

for quantities in range(1, n_lines + 1):
    water = int(input())
    if water <= capacity - cnt_liters:
        cnt_liters += water
    else:
        print("Insufficient capacity!")
print(cnt_liters)
