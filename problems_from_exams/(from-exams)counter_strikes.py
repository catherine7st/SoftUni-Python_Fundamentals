energy = int(input())
command = input()

cnt_battles = 0

while not command == "End of battle":
    distance = int(command)
    if energy < distance:
        print(f"Not enough energy! Game ends with {cnt_battles} won battles and {energy} energy")
        break

    energy -= distance
    cnt_battles += 1

    if cnt_battles % 3 == 0:
        energy += cnt_battles

    command = input()

if command == 'End of battle':
    print(f"Won battles: {cnt_battles}. Energy left: {energy}")
