import re
n = int(input())
p = r"(.+)>([0-9]{3})|([a-z]{3})|([A-Z]{3})|(.{3})<(.+)"
end = ""
for _ in range(0,n):
    data = input()
    v = re.findall(p,data)
    if len(v) != 0 and v[0][0] == v[0][-1] and "<" not in v[0][4] and ">" not in v[0][4]:
        for i in range(1,5):
            end += v[0][i]
        print(f"Password: {end}")
        end = ""

    else:
        print("Try another password!")

import re

lines = int(input())
pattern = r"(.+)>([0-9]{3})|([a-z]{3}|([A-Z]{3}|(.{3}<(.+)"
password = ""

for _ in range(0, lines):
    data = input()
    valid = re.findall(pattern, data)
    if len(valid) != 0 and valid[0][0] == valid[0][-1] and "<" not in valid[0][4] and ">" not in valid[0][4]:
        for i in range(1,5):
            password += valid[0][i]
        print(f"Password: {password}")
        password = ""
    else:
        print("Try another password!")


# import re
#
# lines = int(input())
# pattern = r"(.+)>([0-9]{3})|([a-z]{3}|([A-Z]{3}|(.{3}<(.+)"
# password = ""
#
# for _ in range(0, lines):
#     data = input()
#     valid = re.findall(pattern, data)
#     if len(valid) != 0 and valid[0][0] == valid[0][-1] and "<" not in valid[0][4] and ">" not in valid[0][4]:
#         for i in range(1,5):
#             password += valid[0][i]
#         print(f"Password: {password}")
#         password = ""
#     else:
#         print("Try another password!")