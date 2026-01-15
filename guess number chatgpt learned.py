import os
import random

def diff():
    print("==================")
    print("  Whats the difficulty? ")
    print("==================")
    print("1. Easy")
    print("2. Hard")
    try:
        choice = int(input("Enter Here: "))
    except ValueError:
        print("Please input correct number")
    match choice:
        case 1: return (1,20,5,"easy")
        case 2: return (1,50,10,"hard")
    
    

def play_round(min,max,lives,di):
    number = random.randint(min,max)
    points = 0
    while lives > 0:
        print("==================")
        print("  Guess The Number ")
        print(f"difficulty Level: {di}")
        print(f"Guess: {min} to {max}")
        print(f"Your Life: {lives}")
        print("==================")
        try:
            answer = int(input("Your Guess: "))
        except ValueError:
            print("Please input correct number")
            continue

        if answer == number:
            points = 10
            print(f"Correct Answer you got {points} Points.")
            break
        elif answer > number:
            print("High")
        else:
            print("Low")
        if abs(answer - number) <= 2:
            points += 2
            print(f"Close.")
        lives -= 1
    if lives == 0:
        print(f"Out of lives! The correct number was {number}.")
    return points


def main():
    os.system('cls')
    total_points = 0
    while True:
        print("==================")
        print("  Want to Play? ")
        print(f"Total Points: {total_points}")
        print("==================")
        print("1. Play")
        print("2. Exit")
        try:
            choice = int(input("Enter Here: "))
        except ValueError:
            print("Please input correct number")
            continue

        match choice:
            case 1: 
                min,max,lives,di = diff()
                total_points += play_round(min,max,lives,di)
                print(f"Your Total points is {total_points}")
                input("Press Enter to Continue...")
                os.system('cls')
            case 2:
                print(f"Thanks for playing! Final Score: {total_points}")
                break
            case _:
                print("Invalid choice. Try again.")


main()