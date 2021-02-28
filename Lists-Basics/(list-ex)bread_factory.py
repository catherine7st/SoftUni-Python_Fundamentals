n = int(input())

for row in range(1, n+1):
    for col in range(1, n + 1):
        print(" ", end="")
    print("*"*row)

for neg_row in range(n - 1, 0, -1):
    for neg_col in range(n - neg_row, 1, -1):
        print(" ", end="")
    print("*"*neg_row)


