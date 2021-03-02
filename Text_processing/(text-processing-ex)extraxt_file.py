file = input().split(chr(92))

name, extension = file[-1].split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")
