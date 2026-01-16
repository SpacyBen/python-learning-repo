# Write a program that takes two integers, num1 and num2, as input and checks
# if they have the same sign. If both num1 and num2 are greater than 0 or 
# both are less than 0, it prints "Numbers have the same sign." Otherwise, it does nothing.
# Sample Output 1

# Enter first number: 245
# Enter second number: 3
# Numbers have the same sign.
# Sample Output 2

# Enter first number: -45
# Enter second number: 5
# Sample Output 3

# Enter first number: 0
# Enter second number: 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
    print("Numbers have the same sign.")
    
