students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None }
]
#student represents a variable and index within students 
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")




#------- gets rid of duplicated,   use append instead of add for sets
houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(houses)