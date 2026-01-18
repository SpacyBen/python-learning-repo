import csv
import os

def create_sample_csv(filename, sample_number):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'description', 'price'])
        if sample_number == 1:
            writer.writerow(['Widget', 'A small widget', 19.99])
            writer.writerow(['Widget', 'A small widget', 19.99])
            writer.writerow(['Gadget', 'A handy gadget', 29.99])
            writer.writerow(['Device', 'An electronic device', 39.99])
            writer.writerow(['Gadget', 'A handy gadget', 29.99])

        elif sample_number == 2:
            writer.writerow(['Book', 'An old book', 9.99])
            writer.writerow(['Book', 'An old book', 9.99])
            writer.writerow(['Pen', 'A blue pen', 1.99])
            writer.writerow(['Notebook', 'A spiral notebook', 4.99])
            writer.writerow(['Pen', 'A blue pen', 1.99])
        elif sample_number == 3:
            writer.writerow(['Laptop', 'A gaming laptop', 999.99])
            writer.writerow(['Laptop', 'A gaming laptop', 999.99])
            writer.writerow(['Mouse', 'A wireless mouse', 19.99])
            writer.writerow(['Keyboard', 'A mechanical keyboard', 49.99])
            writer.writerow(['Mouse', 'A wireless mouse', 19.99])
        else:
            writer.writerow(['Phone', 'A smartphone', 699.99])
            writer.writerow(['Phone', 'A smartphone', 699.99])
            writer.writerow(['Tablet', 'A new tablet', 299.99])
            writer.writerow(['Charger', 'A fast charger', 25.99])
            writer.writerow(['Charger', 'A fast charger', 25.99])

def DuplicateRemover(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
    unique_rows = []
    seen = set()
    for row in rows:
        row_tupple = tuple(row)
        if row_tupple not in seen:
            seen.add(row_tupple)
            unique_rows.append(row)
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(unique_rows)
    
            
if __name__ == '__main__':
    for i in range(1, 5):
        create_sample_csv(f'sample{i}.csv', i)

while True:
    inp = input("Enter the filename/path of the CSV file: ")
    try:
        DuplicateRemover(inp)
        print("Duplicate products removed successfully!")
        break
    except FileNotFoundError:
        print("Error: Input file does not exist.")
        continue
