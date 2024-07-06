students = []

with open("students.csv") as file:
    for line in file:
        # Using rows
        """row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")"""
        # Naming the rows' arguments
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")
