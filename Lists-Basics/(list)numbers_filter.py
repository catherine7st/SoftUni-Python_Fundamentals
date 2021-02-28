n = int(input())

even_list = []
odd_list = []
negative = []
positive = []

for num in range(n):
    number = int(input())
    if number % 2 == 0:
        even_list.append(number)
    if not number % 2 == 0:
        odd_list.append(number)
    if number < 0:
        negative.append(number)
    if number >= 0:
        positive.append(number)

word = input()
if word == 'even':
    print(even_list)
elif word == 'odd':
    print(odd_list)
elif word == 'negative':
    print(negative)
elif word == 'positive':
    print(positive)
