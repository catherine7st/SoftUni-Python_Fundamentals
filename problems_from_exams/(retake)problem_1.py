string = input()
command = input()

while not command == "For Azeroth":
    splitted_command = command.split()
    if splitted_command[0] == "GladiatorStance":
        string = string.upper()
        print(string)

    elif splitted_command[0] == "DefensiveStance":
        string = string.lower()
        print(string)

    elif splitted_command[0] == "Dispel":
        index, letter = splitted_command[1:]
        index = int(index)
        if index > len(string):
            print("Dispel too weak.")
        else:
            first_part = string[:index]
            second_part = string[index+1:]
            string = first_part + letter + second_part
            print("Success!")

    elif splitted_command[1] == "Change":
        substring, new_sub = splitted_command[2:]
        string = string.replace(substring, new_sub)
        print(string)

    elif splitted_command[1] == "Remove":
        substring = splitted_command[2]
        string = string.replace(substring, "")
        print(string)

    else:
        print("Command doesn't exist!")

    command = input()
