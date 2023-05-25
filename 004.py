#4.	Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum
#a=input("Enter a: ")
#b=input("Enter b: ")
#c=input("Enter c: ")

a=3
b=4
c=3
sum1 = a+b+c
if(a == b and a == c and b == c):
    print("Sum: ", sum1*3)
else:
    print(sum1)