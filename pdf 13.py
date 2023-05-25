# Write a program that asks the user to enter two integers, obtains the numbers from the
# user, then prints the larger number followed by the words “is larger.” If the numbers are
# equal, print the message “These numbers are equal.” Use only the single-selection form
# of the if statement you learned in this chapter.

a = int(input("Enter number: "))
b = int(input("Enter number: "))
if(a>b):
    print("Number 1 is Greatest")
elif(b>a):
    print("Number 2 is Greatest")
elif(a==b):
    print("Both are Equal")
else:
    print("Invalid Entry")

# Write a program that inputs three different integers from the keyboard (i.e num1, num2,
# num3), then prints the sum, the average, the product, the smallest and the largest of these numbers.
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
add = a+b+c
product = a*b*c
avg = add/3
print("Sum: ",add)
print("Product: ",product)
print("Average: ",avg)
if(a>b and a>c):
    print("Number 1 is Greatest")
elif(b>a and b>c):
    print("Number 2 is Greatest")
else:
    print("Number 3 is Greatest")
if(a<b and a<c):
    print("Number 1 is Smallest")
elif(b<a and b<c):
    print("Number 2 is Smallest")
else:
    print("Number 3 is Smallest")