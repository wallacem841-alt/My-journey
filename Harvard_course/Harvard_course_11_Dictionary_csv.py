import csv

name = input("Name: ")
number = input("Number: ")

# Use 'with' to handle file opening and closing automatically
with open("adress.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, number])