companions = int(input())
days = int(input())

coins = days * 50

for n_day in range(1, days+1):
    if n_day % 10 == 0:
        companions -= 2

    if n_day % 15 == 0:
        companions += 5

    coins -= companions * 2

    if n_day % 3 == 0:
        coins -= companions * 3

    if n_day % 5 == 0:
        coins += 20 * companions

    if n_day % 5 == 0 and n_day % 3 == 0:
        coins -= companions * 2

print(f"{companions} companions received {coins//companions} coins each.")