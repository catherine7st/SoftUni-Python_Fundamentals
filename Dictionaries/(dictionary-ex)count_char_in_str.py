input_line = input()
characters_dict = {}

for char in input_line:
    if char == " ":
        continue

    if char not in characters_dict:
        characters_dict[char] = 0

    characters_dict[char] += 1

for (key, value) in characters_dict.items():
    print(f"{key} -> {value}")

