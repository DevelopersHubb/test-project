#The length & breadth of a rectangle are input through the keyboard. Write a program to
#calculate the area & perimeter of the rectangle.

l = float(input("Enter length: "))
w = float(input("Enter width: "))

area = l * w
peri = 2 * (l + w)

print("Area: ", area)
print("Perimeter: ", peri)

# Round off for 2 decimal places-----------------



#Two numbers (base and exponent) are entered through the keyboard. Write a program to
#find the value of base raised to the power of exponent.

base = 3
exponnt = 4

pwr = 1

for x in range(0, exponnt):
    pwr *= base

print("Answer: ", pwr)

#  suing exponential function