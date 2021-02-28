n = int(input())
a_ascii = ord('a')

for a in range(a_ascii, a_ascii + n):
    for b in range(a_ascii, a_ascii + n):
        for c in range(a_ascii, a_ascii + n):
            print(f"{chr(a)}{chr(b)}{chr(c)}")

