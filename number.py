def main():
    x = get_int()
    print(f"x i {x}")

def get_int():
# A ValueError tells me there's an error with the argument - in this case it's the input format.
# A NameError tells me there's something wrong with my code.
    while True:
        try: 
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main()