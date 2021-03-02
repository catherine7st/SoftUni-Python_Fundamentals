array = list(map(int, input().split()))
command = input().split()

while not command[0] == 'end':
    if command[0] == 'swap':
        array[int(command[1])], array[int(command[2])] = array[int(command[2])], array[int(command[1])]

    elif command[0] == 'multiply':
        array[int(command[1])] *= array[int(command[2])]

    elif command[0] == 'decrease':
        array = [el - 1 for el in array]

    command = input().split()

print(", ".join(list(map(str, array))))
