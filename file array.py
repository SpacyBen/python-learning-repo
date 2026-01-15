items = []

def AddI():
    print("File Add section")
    if not items:
        print("empty")
    else:
        for i, item in enumerate(items, start = 1):
            print(f"{i}. {item}")
    

    addfile = input("add file: ").strip()
    
    items.append(addfile)
    print(f"file added {addfile}")
    



def RemoveI():
    print("File remove section")
    if not items:
        print("empty")
    else:
        for i, item in enumerate(items, start = 1):
            print(f"{i}. {item}")

    choice = int(input("remove file numer: ")) - 1
    if 0 <= choice < len(items):
        remove = items.pop(choice)
    print(f"file removed {remove}")

def EditI():
    print("File edit section")
    if not items:
        print("empty")
    else:
        for i, item in enumerate(items, start = 1):
            print(f"{i}. {item}")

    choice = int(input("edit number: ")) - 1
    if 0 <= choice < len(items):
        previtem = items[choice]
        newitem = input("New Item: ")
        items[choice] = newitem
        print(f"file edited from {previtem} to {newitem}")

while True:
    print("Array File")
    print("1. add file")
    print("2. Remove file")
    print("3. edit file")
    print("0. exit")
    choice = int(input("Enter Here: "))
    match choice:
        case 1: AddI()
        case 2: RemoveI()
        case 3: EditI()
        case 0: break
        case _: print("Input Correct Number")
