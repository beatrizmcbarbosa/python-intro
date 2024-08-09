def main():
    yell("This", "is", "CS50")


def yell(*words):
    # Here I am passing another function to map, referencing it, not calling it - in this case this is upper
    # map will iterate over each of those word, call str.upper on each of those words, and return to me a brand new list containing all of these results
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
