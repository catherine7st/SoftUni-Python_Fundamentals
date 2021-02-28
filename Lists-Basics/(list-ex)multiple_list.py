factor = int(input())
count = int(input())

multiples = []

for num in range(1, count + 1):
    multiples.append(num * factor)

print(multiples)
