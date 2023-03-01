
name = input("Whats your name? ")

if name == "Harry" or "Hermione" or "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slythering")
else:
    print("Who?")


name = input("Whats your name? " )

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")