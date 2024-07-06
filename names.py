# Create the file and add the names
"""name = input("What is your name? ")

# The second argument, w means write, meaning I will be editing the file
# a means append
with open("names.txt", "a") as file:
    file.write(f"{name} \n")"""

# Read through existing names in a file
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
