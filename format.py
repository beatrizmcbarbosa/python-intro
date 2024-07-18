import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
# Group(s) does NOT start counting in 0, it starts in 1
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
