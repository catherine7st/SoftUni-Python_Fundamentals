import re

numbers = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
valid = re.finditer(pattern, numbers)

for v in valid:
    print(v.group(0), end=" ")
