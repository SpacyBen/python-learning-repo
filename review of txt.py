
def AddI():
    print("Current Items")
    with open("Item2.txt","r") as file:
        content = file.readlines()
        if not content:
            print("File Is Empty.")
        for i, content in enumerate(content):
            print(f"{i+1}. {content.strip()}")
        add = input("Add Your Item: ")
        with open("Item2.txt","a") as file:
            file.write(add + "\n")
def RemoveI():
    print("Remove Items")
    with open("Item2.txt","r") as file:
        content = file.readlines()
        if not content:
            print("File Is Empty.")
        for i, line in enumerate(content):
            print(f"{i + 1}. {line.strip()}")
        item = int(input("Remove Item Choose a number: "))- 1
        if 0 <= item < len(content):
            remove = content.pop(item)

            with open("Item2.txt","w") as file:
                file.writelines(content)
            print(f"You Removed {remove.strip()}")

def EditI():
    print("Edit Items")
    with open("Item2.txt","r") as file:
        content = file.readlines()
        if not content:
            print("File Is Empty.")
        for i, line in enumerate(content):
            print(f"{i + 1}. {line.strip()}")
        item = int(input("Edit Item: "))- 1
        if 0 <= item < len(content):
            new_item = input("New Item: ")
            content[item] = new_item

            with open("Item2.txt","w") as file:
                file.writelines(content)
            print(f"Item Edited")
            


while True:
    open("Item2.txt", "a").close()
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Edit Item")
    print("0. exit")
    choice = int(input("Enter Here: "))
    match choice:
        case 1: AddI()
        case 2: RemoveI()
        case 3: EditI()
        case 0: break
        case _: print("Input Correct Number")