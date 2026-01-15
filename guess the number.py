import random

def Game():
    life = 5
    num = random.randint(1,5)
    while life > 0:
        print("Guess the Random Number")
        myguess = int(input("Enter Your Guess: "))
        if myguess == num:
            print("Correct Guess right there.")
            return
        else:
            life -= 1
            print("Wrong Guess Enter again: ")
            print(f"Current Life: {life}")
    
while True:
    print("1. Guessing Game")
    print("2. Exit")
    choice = int(input("enter your choice: "))
    match choice:
        case 1: Game()
        case 2: break
        case _: print("Input correct command")