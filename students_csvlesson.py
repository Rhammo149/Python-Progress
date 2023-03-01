import csv 

students = []


with open ("studentss_csvlesson.csv") as file:
    reader = csv.reader(file)
    for names, home in reader:
        students.append({"names": names, "home": home})
    
    

for student in sorted(students, key=lambda student: student["names"]):
    print(f"{student['names']} is from {student['home']}")


 



       
