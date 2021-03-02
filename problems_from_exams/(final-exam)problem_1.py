data = input()
command = input()

while command != "Done":
    command = command.split()
    if command[0] == "Change":
        for el in data:
            if el == command[1]:
                data = data.replace(el, command[2])
        print(data)

    elif command[0] == "Includes":
        print(command[1] in data)

    elif command[0] == "End":
        print(data.endswith(command[1]))

    elif command[0] == "Uppercase":
        data = data.upper()
        print(data)

    elif command[0] == "FindIndex":
        for el in data:
            if el == command[1]:
                index = data.index(command[1])
                print(index)
                break

    elif command[0] == "Cut":
        start = int(command[1])
        length = int(command[2])
        data = data[start:start+length]
        print(data)

    command = input()
