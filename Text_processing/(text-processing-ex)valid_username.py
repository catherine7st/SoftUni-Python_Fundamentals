usernames = input().split(", ")

names = [name for name in usernames if 3 <= len(name) <= 16 if name.isalnum() or "-" in name or "_" in name]

for name in names:
    print(name)
