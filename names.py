
    # -----------------------------------------------first version (saves the file with the inputs in the different file something.txt, a means append
name = input("whats your name? ")
with open("filenames.txt", "a") as file:
    file.write(f"{name}\n")



    #------------------------------------------- second version (gets rid of unneccesary line, removestrip )

with open("filenames.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())


    #---------------------------------------------third verison (it appends the name to the names list[] and it sorts it alphabetically afterwards and prints)
names = []

with open("filenames.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


    #----------------------------------------------fourth best version if its only one variable like names or change to data(just sort the file)
with open("filenames.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())