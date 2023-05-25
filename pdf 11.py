# Write a program that reads an integer and determines and prints whether it‟s odd or even.
num = int(input("Enter number: "))
if(num % 2== 0):
    print("It is even")
else:
    print("It is odd")

# Write a program that reads in two integers and determines and prints whether the first is a
# multiple of the second. [Hint: Use the remainder operator.
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
if(num2 > num1):
    if(num2 % num1 == 0):
        print("Number 1 is a multiple of number 2")
    else:
        print("Number 1 is not a multiple of number 2")
else:
    print("invelid entry!!!\nNumber 2 can be greater than Number 1")