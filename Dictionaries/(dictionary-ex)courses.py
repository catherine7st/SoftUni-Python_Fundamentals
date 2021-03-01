command = input()
all_courses = {}

while not command == "end":
    course_name, student_name = command.split(" : ")
    if course_name not in all_courses:
        all_courses[course_name] = []
    all_courses[course_name].append(student_name)

    command = input()

for key, value in dict(sorted(all_courses.items(), key=lambda x: -len(x[1]))).items():
    print(f"{key}: {len(value)}")
    for student in sorted(value):
        print(f"-- {student}")


# def get_info(my_dict):
#     for (key, value) in dict(sorted(my_dict.items(), key=lambda el: -len(el[1]))).items():
#         print(f'{key}: {len(value)}')
#         print('--' + ' ' + "\n-- ".join(sorted(value)))
#     return exit()
#
#
# curses = {}
# while True:
#     line = input()
#     if line == "end":
#         get_info(curses)
#     curse_name, user_name = line.split(" : ")
#     if curse_name not in curses:
#         curses[curse_name] = [user_name]
#     else:
#         curses[curse_name] += [user_name]
#
