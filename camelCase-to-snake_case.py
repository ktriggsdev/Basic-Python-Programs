name = input("Enter name of variable in camelCase: ")

j = 0

for char in name:
    if char.isupper():
        print(f"_{char.lower()}", end = "")
    else:
        print(char, end = "")