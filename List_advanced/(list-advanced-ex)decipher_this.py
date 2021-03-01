code = input().split(" ")

for word in code:
    decipher = []
    first_ascii = [ch for ch in word if ch.isdigit()]
    first_ascii = chr(int("".join(first_ascii)))
    decipher += first_ascii
    second_ascii = [al for al in word if al.isalpha()]
    decipher += second_ascii
    decipher[1], decipher[-1] = decipher[-1], decipher[1]
    print("".join(decipher), end=" ")
