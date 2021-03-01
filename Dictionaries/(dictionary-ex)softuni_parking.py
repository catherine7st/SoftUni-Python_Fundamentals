n = int(input())
database = {}

for _ in range(n):
    command = input().split()
    if command[0] == "register":
        user = command[1]
        license_number = command[2]
        if user not in database:
            database[user] = license_number
            print(f"{user} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    elif command[0] == "unregister":
        user = command[1]
        if user not in database:
            print(f"ERROR: user {user} not found")
        else:
            database.pop(user)
            print(f"{user} unregistered successfully")

for user, number in database.items():
    print(f"{user} => {number}")
