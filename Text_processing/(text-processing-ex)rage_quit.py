line = input()
string = ''
result = ''
index = 0

while index < len(line):
    if not line[index].isdigit():
        string += line[index]
        index += 1
    else:
        number = ''
        while index < len(line) and line[index].isdigit():
            number += line[index]
            index += 1
        number = int(number)
        string = string.upper() * number
        result += string
        string = ''

print(f"Unique symbols used: {len(set(result))}")
print(result)
