# Define main function
def main():
    name = input("What's your name? ").strip().title()
    # Split user's name into first and last name
    """first, last = name.split(" ")"""
    hello(name)


# Define function hello()
def hello(to="world"):
    print("hello, ", to)


if __name__ == "__main__":
    main()
