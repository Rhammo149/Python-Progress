# gives the index and the actualy value when enumerate is used, if zip is used with enumerate, you can do it with multiple lists at once

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)


