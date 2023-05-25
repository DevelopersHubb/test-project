#A company insures its drivers in the following cases:
#− If the driver is married.
#− If the driver is unmarried, male & above 30 years of age.
#− If the driver is unmarried, female & above 25 years of age.
#In all other cases, the driver is not insured. If the marital status, sex and age of the driver
#are the inputs, write a program to determine whether the driver is to be insured or not.

m_status = input("Enter marital status: ")
gender = input("Enter gender: ")
age = int(input("Enter age: "))

if(m_status == 'married' or 'Married'):
    print("The driver is insured")
elif(m_status == 'unmarried' or 'Unmarried' and gender == 'male' or 'Male' and age > 30):
    print("The driver is insured")
elif(m_status == 'unmarried' or 'Unmarried' and gender == 'female' or 'Female' and age > 25):
    print("The driver is insured")
else:
    print("The driver is not insured")



#Write a program that take year as an input from user. Determine whether year is leap year or not.
L_year = int(input("Enter Year: "))
if(L_year % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")