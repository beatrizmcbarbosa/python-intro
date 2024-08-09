def main():
    yell(["This", "is", "CS50"])


def yell(words):
    # Initialize the variable uppercase as a list
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
