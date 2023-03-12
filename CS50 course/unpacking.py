# star symbol unpacks it and treats it separately
   

def total(gold, silver, bronze):
    return(gold * 17 + silver) * 29 + bronze

coins = [100, 50, 25]

print(total(*coins), "Bronze coins")


#------------------------------- use two asterisks when unpacking dictionaries

def total(gold, silver, bronze):
    return(gold * 17 + silver) * 29 + bronze

coins = {"gold": 100, "silver": 50, "bronze": 25}

print(total(**coins), "Bronze coins")

#---------------------------------- *args and **kwargs makes it so the output doesnt have to match the arguments in the function

def f(*args, **kwargs):
    print("Named:", kwargs)

f(gold=100, silver=50, bronze=25)



