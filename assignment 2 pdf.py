#The distance between two cities (in km.) is input through the keyboard. Write a program
#to convert and print this distance in meters, feet, inches and centimeters.


dis = float(input("Enter Distance = "))

m = dis * 1000
cm = dis * 1000 * 100
f = dis * 3280.84
inch = dis * 39370.08

print("Distance in Feet= ", f)
print("Distance in Inches= ", inch)
print("Distance in Meters= ", m)
print("Distance in Centimeters= ", cm)

# Round off for 2 decimal places
