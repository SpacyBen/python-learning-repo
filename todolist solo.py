import os
def add_list():
    print("Your To-Do list")
    try:
        #show list
        with open("File.txt","r") as file:
            content = file.readlines()
        if not content:
            print("no list yet")
        for i, content in enumerate(content):
            print(f"{i+1}. {content.strip()}")
        #add item from list
        list = input("Add to-do on list: ")
        with open("File.txt","a") as file:
            file.write(list +"\n")
        print(f"You added {list} from Your List")


    except FileNotFoundError:
        print("No list found")

    

def remove_list():
    print("Your To-Do list")
    try:
        #show list
        with open("File.txt","r") as file:
            content = file.readlines()
        if not content:
            print("no list yet")
        for i, line in enumerate(content):
            print(f"{i+1}. {line.strip()}")
        #remove item from list
        list = int(input("Select number on list to remove: ")) - 1
        if 0 < list < len(content):
            with open("File.txt","w") as file:
                removed = content.pop(list)
                file.writelines(content)
                print(f"You Removed {list}. {removed.strip()}from Your List")
            input("Enter")
    except FileNotFoundError:
        print("No list found")

    
def edit_list():
    print("Your To-Do list")
    try:
        with open("File.txt","r") as file:
            content = file.readlines()
        if not content:
            print("no list yet")
        for i, content in enumerate(content):
            print(f"{i+1}. {content.strip()}")
        
        

    except FileNotFoundError:
        print("No list found")

    


while True:
    os.system("cls")
    print("================")
    print("   To Do List   ")
    print("================")
    print("1. Add list")
    print("2. Remove list")
    print("3. Edit list")
    print("0. Exit")
    choose = int(input("Enter Here: "))
    match choose:
        case 1: 
            add_list()
        case 2: 
            remove_list()
        case 3: 
            edit_list()
        case 0: 
            break
        case _: 
            print("Input correct number")

