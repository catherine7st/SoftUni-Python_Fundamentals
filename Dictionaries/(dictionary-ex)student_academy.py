n = int(input())

students = {}

for _ in range(n):
    (student, grade) = (input(), float(input()))
    if student not in students:
        students[student] = []
    students[student].append(grade)

average_students = dict((key, sum(value) / len(value)) for (key, value) in students.items())
filtered_average_students = dict((key, value) for (key, value) in average_students.items() if value >= 4.50)

for (key, value) in sorted(filtered_average_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{key} -> {value:.2f}")

#
# n = int(input())
#
# students = {}
#
# for _ in range(n):
#     name = input()
#     grade = float(input())
#
#     if name not in students:
#         students[name] = []
#     students[name].append(grade)
#
# filtered_students = {}
#
# for student, grades in students.items():
#     average_grade = sum(grades) / len(grades)
#     if average_grade >= 4.50:
#         filtered_students[student] = average_grade
#
# for student, av_grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
#     print(f"{student} -> {av_grade:.2f}")
#
