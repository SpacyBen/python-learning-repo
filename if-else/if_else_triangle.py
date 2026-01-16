# Is The Triangle Equilateral?
# by CodeChum Admin

# Write a program that takes three integers x, y, and z,
# as input and checks if they represent the sides of an equilateral triangle. 
# An equilateral triangle has all sides of equal length, so this function checks 
# if x, y, and z are all equal. If they are equal, it prints "Triangle is equilateral."
# Otherwise, it does nothing.

# Sample Output 1
# Enter x: 10
# Enter y: 5
# Enter z: 4

# Sample Output 2
# Enter x: 5
# Enter y: 5
# Enter z: 5
# Triangle is equilateral.

# Sample Output 3
# Enter x: 4
# Enter y: 4
# Enter z: 4
# Triangle is equilateral.

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
if x == y == z:
    print("Triangle is equilateral.")