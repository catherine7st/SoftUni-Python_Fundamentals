string = input()
now_str = ""

for letter in range(0, len(string)):
    now_str += string[letter] * 2
print(f'{now_str}')
