password = input().strip()

password = [ord(el) + 3 for el in password]
password = [chr(el) for el in password]

print("".join(password))
