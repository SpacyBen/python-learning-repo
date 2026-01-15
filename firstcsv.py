import csv

listof = []
with open("file.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["column1", "column2" , "column3"])

someting = input("Enter something you want to write: ")
someting2 = input("Enter something2 you want to write: ")
someting3 = input("Enter something3 you want to write: ")
with open("file.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([someting, someting2, someting3])
editcol2 = int(input("edit col: "))
editrow= int(input("edit row: "))
editput= input("Enter new value: ")
with open("file.csv", "r", newline="") as file:
    reader = csv.reader(file)
    listof = list(reader)

listof[editcol2][editrow] = editput

with open("file.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(listof)
    




print(listof)
