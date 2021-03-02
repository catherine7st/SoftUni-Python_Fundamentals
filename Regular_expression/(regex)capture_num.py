import re

line = input()
p = r"\d+"
numbers = []

while line:
    match = re.findall(p, line)
    if match:
        numbers.extend(match)

    line = input()

print(" ".join(numbers))

