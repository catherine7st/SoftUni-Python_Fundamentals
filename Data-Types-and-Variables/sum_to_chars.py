lines = int(input())
sum_chars = 0

for i in range(1, lines + 1):
    letter = input()
    sum_chars += ord(letter)

print(f"The sum equals: {sum_chars}")