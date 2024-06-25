import random

cards = ["jack", "queen", "king"]

def main():
    print(random.choices(cards, weights=[70, 15, 15], k=2))


main()