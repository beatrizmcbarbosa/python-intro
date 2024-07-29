def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Here I am returning one value which is a tuple. And within this tupple, there are two values.
    return (name, house)


if __name__ == "__main__":
    main()
