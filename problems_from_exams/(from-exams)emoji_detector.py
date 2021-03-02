main_text = input().split()
multiply_nums = 1
cnt_emojis = 0
emojis = []
sum_ord_emoji = 0
cool_emojis = []

for word in main_text:
    for index in word:
        if index.isdigit():
            index = int(index)
            multiply_nums *= int(index)

    if word[-1] == ",":
        word = word[:-1]

    if word[2:-2].isalpha():

        if word.startswith('::') and word.endswith('::') and word[2].isupper():
            emojis.append(word)
            cnt_emojis += 1

        elif word.startswith('**') and word.endswith('**') and word[2].isupper():
            emojis.append(word)
            cnt_emojis += 1

for emoji in emojis:
    if emoji[2:-2].isalpha():
        for i in emoji[2:-2]:
            sum_ord_emoji += ord(i)

        if sum_ord_emoji >= multiply_nums:
            cool_emojis.append(emoji)
            sum_ord_emoji = 0

print(f"Cool threshold: {multiply_nums}")
print(f"{cnt_emojis} emojis found in the text. The cool ones are:")
for el in cool_emojis:
    print(el)
