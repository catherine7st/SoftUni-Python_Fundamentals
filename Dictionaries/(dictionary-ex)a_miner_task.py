data = input()
resources = {}

while not data == "stop":
    (resource, quantity) = (data, int(input()))
    if resource not in resources:
        resources[resource] = 0
    resources[resource] += quantity

    data = input()

for (resource, quantity) in resources.items():
    print(f"{resource} -> {quantity}")
