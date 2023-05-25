# Write a program that calculates the squares and cubes of the numbers from 0 to 10 and
# uses tabs to print the following table of values:
n=10
print("number\tsquare\tcube")
for x in range(0, n+1):
    print(x, "\t", x*x, "\t", x*x*x)

# Write a program that calculates and prints the sum of the even integers from 2 to 30.
sum = 0
n=30
for x in range(2, n+1):
    if(x % 2 == 0):
        sum = sum + x
print("Sum =", sum)

# Write a program to enter the numbers till the user wants and at the end it should display
# the count of positive, negative and zeros entered.
num = []
count = 0
count1 = 0
count2 = 0
number = int(input("Enter Numbers: "))
for n in range(0, number):
    num.insert(n, int(input()))
for x in range(0, len(num)):
    if(num[x] > 0):
        count += 1
    if(num[x] < 0):
        count1 += 1
    if(num[x] == 0):
        count2 += 1
    else:
        print("Invalid Entry")
print("Positive numbers", count)
print("Negative numbers", count1)
print("Zeros are", count2)