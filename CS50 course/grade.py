score = int(input("Score: "))


while score <= 60:
    print("Grade: F")
    exit()

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
