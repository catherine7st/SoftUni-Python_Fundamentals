people = int(input())
capacity = int(input())

courses = people // capacity
if people % capacity == 0:
    print(courses)
else:
    print(courses + 1)
