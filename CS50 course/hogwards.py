students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)



for i in range(len(students)):
    print(i + 1, students[i])

 


 #dictionary is used when you want to associate multiple things to something use  variable = {" ", " ", } for dictionary
# below is a dictionary that is within a list, dictionaries help you get to data quickly

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None }
]
#student represents a variable and index within students 
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")










students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
}

for student in students:
    print(student, students[students], sep=", ")

