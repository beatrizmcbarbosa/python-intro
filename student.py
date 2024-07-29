class Student: ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    # An object is the same as an instance
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
