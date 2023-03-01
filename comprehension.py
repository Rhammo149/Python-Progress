 #-------------------------------- list comprehension
    
def main():
    yell("Hi", "you")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    

if __name__ == "__main__":
    main()

#---------------------------dic comprehension                  comprehension are like conditionals withous using if, for, etc statements

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

