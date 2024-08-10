students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


def is_gryffindor(s):
    # Here I am returning the value of the boolean in a simplified manner
    # If the student house is gryffindor, return. If False, do nothing. That's basically what it's saying
    return s["house"] == "Gryffindor"


# Similar to map, I am passing a function that is going to apply to every student in my list
# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not
gryffindors = filter(is_gryffindor, students)

# I can sort a list in a dictionary using the below syntax
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
