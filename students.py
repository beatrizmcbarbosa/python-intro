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

# Lambda introduces the concept of anonymous functions.
# You can use lambda as many times as you want.
# If lambda requires multiple paramenters, you can use commas, e.g.:
# lambda student, x, y: ...
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")
