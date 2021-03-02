import re

pattern = r"(^|(?<=\s))\|(?P<boss>[A-Z]{4,})\|:#(?P<title>[A-Za-z]+\s[A-Za-z]+)#($|(?=\s))"

n = int(input())

for _ in range(n):
    line = input()
    if re.search(pattern, line) is None:
        print("Access denied!")
    else:
        matches = re.finditer(pattern, line)
        for match in matches:
            result = match.groupdict()
            if result:
                print(f"{result['boss']}, The {result['title']}")
                print(f">> Strength: {len(result['boss'])}")
                print(f">> Armour: {len(result['title'])}")
