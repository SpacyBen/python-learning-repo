import random
import os





def diff():
    global diffstate
    print('==========')
    print('1. Easy')
    print('2. Hard')
    choice = int(input('Enter your Choice: '))
    match choice:
        case 1: 
            diffstate = 1
            guess()
        case 2: 
            diffstate = 2
            guess()
        case _: print("invalid choice")


def guess():
        randomnum1 = random.randint(1,20)
        randomnum2 = random.randint(1,50)
        guesstype2 = 'Guess Hard: 1 to 50'
        guesstype1 = 'Guess Easy: 1 to 20'  
        points = 0
        life = 5
        if diffstate == 1:
            randomnum = randomnum1
        elif diffstate == 2:
            randomnum = randomnum2

        while life > 0:
            print('=================')
            if diffstate == 1:
                print(guesstype1)
            if diffstate == 2:
                print(guesstype2)
            guess = int(input('Whats your guess: '))
            if guess == randomnum:
                print('Answer: correct')
                points = 10
                print(f"Current points: {points}")
                print(f"Current life: {life}")
                input("Press Enter to Continue...")
                break
            elif guess > randomnum:
                print('Answer: Lower')
                if guess == randomnum - 3 or guess == randomnum + 3:
                    print('Try again its close + 1 points. ')
                    points = points + 1
                life = life - 1
                print(f"Current points: {points}")
                print(f"Current life: {life}")
            elif guess < randomnum:
                print('Answer: Higher')
                if guess == randomnum - 1 or guess == randomnum + 1:
                    print('Try again its close + 2 points. ')
                    points = points + 2
                life = life - 1
                print(f"Current points: {points}")
                print(f"Current life: {life}")
            if life == 0:
                print(randomnum)
                print('No more points')
                input("Press Enter to Continue...")



while True:
    os.system('cls')
    print('==========')
    print('1. Guessing Game')
    print('2. exit')
    choice = int(input('Enter your Choice: '))
    match choice:
        case 1: diff()
        case 2: break
        case _: print("invalid choice")