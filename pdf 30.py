# Write a program that takes the side of a square from user and then prints that square out
# of asterisks. Your program should work for squares of all side sizes between 1 and 20.
num = int(input("Enter number: "))
for x in range(0, num):
    for y in range(0, num):
        print("*", end= '')
    print("\r")

# Write a program that displays the following checkerboard pattern:
x = 8
y = 8

for x1 in range(0, x):
    for y1 in range(0, y):
        print("*", end='')
        y -= 1
    
    print("\n")
    if(x % 2 == 0):
        print(end=' ')
    y = 8
    x -= 1