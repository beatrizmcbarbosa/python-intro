def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        # yield is telling the program: "Return one value at a time", rather than having the program waiting to generate all of them to print them in the terminal
        # this will be useful to print very large amounts of sheep
        yield "🐑" * i
    return flock


if __name__ == "__main__":
    main()
