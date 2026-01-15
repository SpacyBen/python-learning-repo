def add_item():
    try:
        print("\nYour items:")
        with open("File.txt", "r") as file:
            content = file.readlines()
        for i , line in enumerate(content):
            print(f"{i+1}. {line.strip()}")
        item = input("Add your Item: ")
        if item.strip()=="":
            print("It must not blank")
        else:
            with open("File.txt","a") as file:
                file.write(item + "\n")
            print("Item Saved.")
    except FileNotFoundError:
        print("No items yet!")
def remove_item():
    print("\nYour items:")
    try:
        with open("File.txt", "r") as file:
            content = file.readlines()
        if not content:
            print("No item")
            return
        for i, line in enumerate(content):
            print(f"{i+1}. {line.strip()}")
        item = int(input("Remove Item: ")) - 1
        if 0 <= item < len(content):
            removed = content.pop(item)

            with open("File.txt", "w") as file:
                file.writelines(content)
            print(f"Item Removed: {removed.strip()}")
        else:
            print("Invalid no Item listed there")

    except FileNotFoundError:
        print("No items yet!")
def edit_item():
    print("\nYour items:")
    try:
        with open("File.txt", "r") as file:
            content = file.readlines()
        if not content:
            print("No item")
            return
        for i, line in enumerate(content):
            print(f"{i+1}. {line.strip()}")
        item = int(input("Choose Number Do you want to change: ")) - 1
        if 0 <= item < len(content):
            new_item = input("Change Item: ")
            content[item] = new_item + "\n"

            with open("File.txt", "w") as file:
                file.writelines(content)
            print(f"Item Edited: {new_item.strip()}")
        else:
            print("Invalid no Item listed there")

    except FileNotFoundError:
        print("No items yet!")
    

while True:
    print("File Manager")
    print("1. Add File")
    print("2. remove File")
    print("3. Edit File")
    print("0. Exit")
    try: 
        choose = int(input("Enter What You want: "))
    except ValueError:
        print("Invalid Number")
        continue

    match choose:
        case 1:
            add_item()
        case 2:
            remove_item()
        case 3:
            edit_item()
        case 0:
            break
        case _:
            print("Invalid Number")




