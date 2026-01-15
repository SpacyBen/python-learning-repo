import os
def cal1():
    while True:
        print('Please Choose')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Devide')
        print('0. Exit \n')
        

        try:
            choice = int(input('Enter your Choice: '))
        except ValueError:
            print('Please enter Number')
            continue

        match choice:
            case 1:
                num1, num2 = get_numbers
                result = num1 + num2
                print(f"The answer is: {result}")
            case 2:
                num1, num2 = get_numbers
                result = num1 - num2
                print(f"The answer is: {result}")
            case 3:
                num1, num2 = get_numbers
                result = num1 * num2
                print(f"The answer is: {result}")
            case 4:
                num1, num2 = get_numbers
                result = num1 / num2
                print(f"The answer is: {result}")
            case 0:

                print('exited')
                break
            case _:
                print('input correct number')
def get_numbers():
    num1 = float(input('Enter Num1: '))
    num2 = float(input('Enter Num2: '))
    return num1, num2

def cal2():
    num1 = float(input('Enter Num1: '))
    op = input('Enter Operator: ')
    if op in ['+', '-', '*', '/']:
        num2 = float(input('Enter Num2: '))
        match op:
            case '+':
                result = num1 + num2
                print(f"The answer is: {result}")
                input("Press Enter to continue...")
                os.system('cls')
            case '-':
                result = num1 - num2
                print(f"The answer is: {result}")
                input("Press Enter to continue...")
                os.system('cls')
            case '*':
                result = num1 * num2
                print(f"The answer is: {result}")
                input("Press Enter to continue...")
                os.system('cls')
            case '/':
                result = num1 / num2
                print(f"The answer is: {result}")
                input("Press Enter to continue...")
                os.system('cls')
                #on input("Press Enter to continue...")
                #os.system('cls')
                # i can just make anther function like def continue()

    else:
        os.system('cls')
        print('You input Wrong number please try again `\n')
        
os.system('cls')
while True:
    print('Please Choose')
    print('1. calculator1')
    print('2. calculator2')
    print('0. Exit \n')
    try:
        choice = int(input('Enter your Choice: '))
    except ValueError:
        print('Please enter Number')
        continue
    match choice:
        case 1:
            cal1()
        case 2:
            cal2()
        case 0:
            os.system('cls')
            print('exited')
            break
        case _:
            print('input correct number')
        



    
    

