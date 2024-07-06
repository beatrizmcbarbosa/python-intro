import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(
            {"name": row["name"], "home": row["home"], "house": row["house"]}
        )

# Lambda introduces the concept of anonymous functions.
# You can use lambda as many times as you want.
# If lambda requires multiple paramenters, you can use commas, e.g.:
# lambda student, x, y: ...
for student in sorted(students, key=lambda student: student["name"]):
    print(
        f"{student['name']} is from {student['home']} and now lives in {student['house']}"
    )
