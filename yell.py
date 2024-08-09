def main():
    yell("This", "is", "CS50")


def yell(*words):
    # list comprehensions. Here I am doing the exact same thing. I am turning upper each of the words in the words list, the words list was passed into yell (i.e. yell(*words))
    # The below means "give me the upper case version for each word in the words list"
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
