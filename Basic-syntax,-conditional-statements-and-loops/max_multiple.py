# divisor = int(input())
# bound = int(input())
# n = 0
#
# for num in range(bound, 0, -1):
#     if num % divisor == 0:
#         print(num)
#         break

divisor = int(input())
bound = int(input())

result = int(bound/divisor) * divisor
print(result)