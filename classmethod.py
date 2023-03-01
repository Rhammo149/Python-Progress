import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod  
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
        
#--------- class method is used because there is only one "Hat" that sorts a student randomly to a house
#--------- previously, it was a instance method called class Student because there is more than one student, 
#--------- There is a blueprint for student like an actual real houses because it uses decorators like paint = house
#--------  there is a blueprint student, because the student might belong to a different house or address and have different names (Different type of students)
#-------- in the case of Hat, its all the same Hat. (There is no different type of a Hat)

Hat.sort("Harry")
