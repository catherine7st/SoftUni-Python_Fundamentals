health = 100
bitcoins = 0
cnt_rooms = 0

rooms = input().split("|")

for room in rooms:
    action, energy = room.split()
    energy = int(energy)
    cnt_rooms += 1

    if action == 'potion':

        if health + energy > 100:
            energy = 100 - health
        health += energy
        print(f"You healed for {energy} hp.")
        print(f"Current health: {health} hp.")

    elif action == 'chest':
        bitcoins += energy
        print(f"You found {energy} bitcoins.")

    else:
        health -= energy

        if health <= 0:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {cnt_rooms}")
            break
        else:
            print(f"You slayed {action}.")

if health > 0:
    print(f'You\'ve made it!\nBitcoins: {bitcoins}\nHealth: {health}')
