def main():
    print_square(3)

#1 Print a square
"""def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        print()"""
    
#2 Another way of printing square as above
"""def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)"""

#3 Simplest way print square as above
def print_square(size):
    for i in range(size):
        print("#" * size)

# Print in horizontal lines
"""def print_row(width):
    for _ in range(width):
        print("#")
"""

main()
