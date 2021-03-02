line = input()
records = {}
while line != 'Log out':
    data = line.split(': ')
    command = data[0]
    username = data[1]
    if command == 'New follower':
        if username in records:
            pass
        else:
            records[username] = 0
    if command == 'Like':
        if username in records:
            records[username] += int(data[2])
        else:
            records[username] = int(data[2])
    if command == 'Comment':
        if username in records:
            records[username] += 1
        else:
            records[username] = 1
    if command == 'Blocked':
        if username in records:
            del records[username]
        else:
            print(f'{username} doesn\'t exist.')

    line = input()

print(f'{len(records)} followers')

sorted_users = sorted(records.items(), key=lambda x: (-x[1], x[0]))

for user, cnt in sorted_users:
    print(f'{user}: {cnt}')