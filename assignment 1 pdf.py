#Write a program that asks the user to enter two numbers, obtains them from the user and
#prints their sum, product, difference, quotient and remainder

a = float(input("Enter 1st Number: "))
b = float(input("Enter 2nd Number: "))

add = a + b
pro = a * b
diff = a - b
remain = a % b
quoti = a // b

print("Sum = ", add)
print("Product = ", pro)
print("Difference = ", diff)
print("Remainder = ",remain)
print("Quotient = ",quoti)

# Round off for 2 deciaml places