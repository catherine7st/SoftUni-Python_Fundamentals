# line = input().split(">")
# explose = 0
# after_explose = []
# for chars in line:
#     if chars[0].isdigit():
#         explose += int(chars[0])
#         if len(chars) <= explose:
#             explose -= len(chars)
#             chars = ">"
#         else:
#             chars = ">" + "".join(list(chars[explose::]))
#             explose = 0
#     after_explose.append(chars)
# print("".join(after_explose))
#
#
# text = input()
# result = ""
# force = 0
# i = 0
# while i < len(text):
#     if text[i] != ">":
#         result += text[i]
#         i += 1
#     else:
#         result += ">"
#         i += 1
#         force += int(text[i])
#         while force > 0 and text[i] != ">":
#             i += 1
#             force -= 1
#             if i >= len(text):
#                 break
# print(result)

line = input()
power = 0

for i in range(len(line)):
    el = line[i]
    if el == ">":
        if line[i + 1].isdigit():
            power += int(line[i + 1])
    elif power > 0:
        line = line[:i] + "x" + line[i + 1:]
        power -= 1

print(line.replace("x", ""))
