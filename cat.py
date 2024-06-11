# While loop
"""i=0
while i<3:
    print("meow")
    i+=1
"""

# For loop: first option is hard to read, second is good
"""print("meow\n" * 3, end="")
"""
"""for _ in range(3):
    print("meow")"""

# Validating input
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("How many meows? "))
        if n>0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")
