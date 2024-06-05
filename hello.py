# Define main function
def main():
    name = input ("What's your name? ").strip().title()
    # Split user's name into first and last name
    first, last = name.split(" ")
    hello(first)

# Define function hello()
def hello(to="world"):
    print("hello, ", to)


main()