def main():
    x = get_int("What's x? ")
    print(f"x i {x}")

def get_int(prompt):
# A ValueError tells me there's an error with the argument - in this case it's the input format.
# A NameError tells me there's something wrong with my code.
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")
            # I could just use "pass" instead to avoid the repetition of "x is not an integer". It might be more user friendly.
"""            pass
"""
main()