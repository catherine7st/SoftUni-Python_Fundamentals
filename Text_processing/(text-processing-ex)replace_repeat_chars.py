string = input()
new_string = ""
new_letter = ""

for letter in string:
    if not letter == new_letter:
        new_string += letter
    new_letter = letter

print(new_string)
