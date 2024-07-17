import re

email = input("What's your email? ").strip()

# What is in the parenthesis, (\w+\.)? can either be there once or not at all
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
