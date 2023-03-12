import csv

name = input("whats your name? ")
home = input("wheres your home? ")


with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})