number_of_rooms = int(input())
free_chairs = 0
needed_chairs_in_room = 0

for room in range(1, number_of_rooms + 1):
    data = input()
    num_chairs, taken_chairs = data.split()
    taken_chairs = int(taken_chairs)
    if len(num_chairs) > taken_chairs:
        free_chairs += len(num_chairs) - taken_chairs
    elif len(num_chairs) < taken_chairs:
        needed_chairs_in_room = 0
        needed_chairs_in_room += taken_chairs - len(num_chairs)
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")

if needed_chairs_in_room == 0:
    print(f"Game On, {free_chairs} free chairs left")
