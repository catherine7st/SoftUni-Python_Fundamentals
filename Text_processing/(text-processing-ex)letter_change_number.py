position_alpha = {chr(el+97): el+1 for el in range(26)}
data = input().split()
result = 0

for el in data:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])
    if first_letter.isupper():
        number /= position_alpha[first_letter.lower()]
    elif first_letter.islower():
        number *= position_alpha[first_letter]

    if last_letter.isupper():
        number -= position_alpha[last_letter.lower()]
    elif last_letter.islower():
        number += position_alpha[last_letter]

    result += number
print(f"{result:.2f}")
