command = input()
heroes = {}

while not command == "End":
    splitted_command = command.split()
    if splitted_command[0] == "Enroll":
        name = splitted_command[1]
        if name in heroes:
            print(f"{name} is already enrolled.")
        else:
            heroes[name] = []

    elif splitted_command[0] == "Learn":
        name, spell_name = splitted_command[1:]
        if name not in heroes.keys():
            print(f"{name} doesn't exist.")
        else:
            if spell_name in heroes[name]:
                print(f"{name} has already learnt {spell_name}.")
            else:
                heroes[name] = spell_name
    elif splitted_command[0] == "Unlearn":
        name, spell_name = splitted_command[1:]

        if name not in heroes:
            print(f"{name} doesn't exist.")
        else:
            
            else:
                print(f"{name} doesn't know {spell_name}.")
    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0]))

print("Heroes:")
for heroe, value in sorted_heroes:
    if len(value) == 0:
        print(f"== {heroe}:")
    else:
        print(f"== {heroe}: {value}")
