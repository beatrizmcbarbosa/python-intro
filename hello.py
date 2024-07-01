# Define main function
def main():
    name = input("What's your name? ").strip().title()
    # Split user's name into first and last name
    """first, last = name.split(" ")"""
    print(hello(name))


# Define function hello()
def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()
