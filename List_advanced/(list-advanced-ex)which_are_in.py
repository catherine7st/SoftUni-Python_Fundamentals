# substrings = input().split(', ')
# words = input().split(', ')
#
# result = [subst for subst in substrings for word in words if subst in word]
#
# print(sorted(set(result), key=result.index))
#
#
first_string = input().split(", ")
second_string = input()

words = list(filter(lambda x: x in second_string, first_string))

print(words)
