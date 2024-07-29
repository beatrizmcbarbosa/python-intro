def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    # Can also represent a tuple like this. When to use tuple vs list? When I know the value can change.
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Here I am returning one value which is a tuple. And within this tupple, there are two values.
    return [name, house]


if __name__ == "__main__":
    main()
