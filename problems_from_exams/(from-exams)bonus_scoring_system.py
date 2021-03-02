number_of_students = int(input())
lectures = int(input())
bonus = int(input())
n_attendances = 0
max_bonus = 0

while not number_of_students == 0:
    attendances = int(input())

    current_bonus = attendances / lectures * (5 + bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        n_attendances = attendances

    number_of_students -= 1

print(f"Max Bonus: {round(max_bonus)}.\nThe student has attended {n_attendances} lectures.")
