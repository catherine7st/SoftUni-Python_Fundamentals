import re

command = input()
pattern = r"^>{2}(?P<kind>\w+)<{2}(?P<price>[0-9]+(\.\d+)?)\!(?P<quantity>\d+)($|\s)"
furniture = []
total_price = 0

while not command == "Purchase":
    match = re.match(pattern, command)
    if match:
        product = match.groupdict()
        furniture.append(product["kind"])
        total_price += float(product["price"]) * int(product["quantity"])

    command = input()

print("Bought furniture:")
for pr in furniture:
    print(pr)
print(f"Total money spend: {total_price:.2f}")
