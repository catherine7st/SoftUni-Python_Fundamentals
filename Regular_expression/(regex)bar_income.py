import re

line = input()
pattern = r"%(?P<name>[A-Z][a-z]*)%.*?<(?P<product>\w.*?)>.*?\|(?P<count>\d+?)\|.*?(?P<price>\d+\.?\d+)\$"
total_price = 0
income = 0

while not line == "end of shift":
    match = re.match(pattern, line)
    if match:
        result = match.groupdict()
        total_price = int(result["count"]) * float(result["price"])
        print(f"{result['name']}: {result['product']} - {total_price:.2f}")
        income += total_price

    line = input()

print(f"Total income: {income:.2f}")
