start_key = input()
command = input()

while not command == "Generate":
    command_type = command.split(">>>")[0]

    if command_type == "Contains":
        substring = command.split(">>>")[1]
        if substring in start_key:
            print(f"{start_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command_type == "Flip":
        command_type, upper_or_lower, start_index, end_index = command.split(">>>")
        start_index = int(start_index)
        end_index = int(end_index)
        if upper_or_lower == "Upper":
            start_key = start_key[:start_index] + start_key[start_index:end_index].upper() + start_key[end_index:]
            print(start_key)
        elif upper_or_lower == "Lower":
            start_key = start_key[:start_index] + start_key[start_index:end_index].lower() + start_key[end_index:]
            print(start_key)

    elif command_type == "Slice":
        command_type, start_index, end_index = command.split(">>>")
        start_index = int(start_index)
        end_index = int(end_index)
        start_key = start_key[:start_index] + start_key[end_index:]
        print(start_key)

    command = input()

print(f"Your activation key is: {start_key}")
