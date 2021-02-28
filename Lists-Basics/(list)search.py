n = int(input())
word = input()

all_strings = []
str_with_word = []

for n in range(n):
    string = input()
    all_strings.append(string)
    if word in string:
        str_with_word.append(string)

print(all_strings)
print(str_with_word)

