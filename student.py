class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def house(self):
        # The _ is used because I can't have both the property and the instance variable both called house, python will confuse one for the other
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    # An object is the same as an instance
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
