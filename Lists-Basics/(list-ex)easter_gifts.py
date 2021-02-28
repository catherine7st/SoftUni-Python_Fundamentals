gifts = input().split(" ")
command = input()

while not command == "No Money":
    if 'OutOfStock' in command:
        name_command, gift = command.split()
        for index1 in range(len(gifts)):
            if gifts[index1] == gift:
                gifts[index1] = "None"
    elif 'Required' in command:
        name_command, gift, index = command.split()
        index = int(index)
        if index < len(gifts):
            gifts[index] = gift
    elif 'JustInCase' in command:
        name_command, gift = command.split()
        gifts.pop()
        gifts.append(gift)
    command = input()

for el in gifts:
    if "None" in gifts:
        gifts.remove("None")

new_gifts_list = " ".join(gifts)

print(new_gifts_list)