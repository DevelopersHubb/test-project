# 1.	Write a Python program which accepts the user's first and last name and 
# print them in reverse order with a space between them

Fname = input("Enter first name: ")
Lname = input("Enter last name: ")
f_name = Fname + " " + Lname
str1 = f_name[::-1]

print("In reverse order : ", str1)

# remove range and extra variables

# done