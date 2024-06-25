students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Eussel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

# Print name, house, patronus
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# Print name and house (there was no patronus)
"""for student in students:
    print(student, students[student], sep=", house: ")"""

# Print existing students (there was no house")
"""for student in students:
    print(student)"""

# Print existing students (there was no house")
"""for i in range(len(students)):
    print(i+1, students[i])"""
