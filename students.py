import csv 

students = []


with open ("studentss.csv") as file:
    reader = csv.reader(file)
    for names, home in reader:
        students.append({"names": names, "home": home})
    
    

for student in sorted(students, key=lambda student: student["names"]):
    print(f"{student['names']} is from {student['home']}")

#dict reader version allowes for more flexibility   studentss.csv
# in the csv file, just add names,home at the top, dict helps it to break less even with changes like adding new colums and flipping stuff

reader = csv.DictReader(file)
for row in reader:
    students.append({"names": row["names"], "home": row["home"]})

 



       
