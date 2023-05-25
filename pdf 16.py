# Write a program to check whether a triangle is valid or not, when the three angles of the
# triangle are entered through the keyboard. A triangle is valid if the sum of all the three
# angles is equal to 180 degrees.

a = float(input("Enter Angle 1: "))
b = float(input("Enter Angle 2: "))
c = float(input("Enter Angle 3: "))
add = a+b+c
if(add == 180):
    print("Valid Triangle")
else:
    print("Invalid Triangle")

# Given the length and breadth of a rectangle, write a program to find whether the area of
# the rectangle is greater than its perimeter. For example, the area of the rectangle with
# length = 5 and breadth = 4 is greater than its perimeter.
length = float(input("Enter length: "))
width =  float(input("Enter width: "))
area = length * width
peri = 2 * (length + width)
if(area > peri):
    print("Area is greater than its Perimeter")
else:
    print("Perimeter is greater than its Area")

# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is isosceles, equilateral, scalene or right-angled triangle.
a = float(input("Enter Angle 1: "))
b = float(input("Enter Angle 2: "))
c = float(input("Enter Angle 3: "))
if(a == b and b == c):
    print("Triangle is Equilateral")
elif(a == b or b == c or c == a):
    print("Triangle is isoceles")
elif(a == 90 or b == 90 or c == 90):
    print("Right angled Triangle")
else:
    print("Triangle is scalene")