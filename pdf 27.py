# Develop a program that will determine the gross pay for each of several employees. The
# company pays “straight time” for the first 40 hours worked by each employee and pays
# “time-and-a-half” for all hours worked more than 40 hours.

hours = int(input("Enter number of hours worked (-1 to end): " ))
rate = int(input("Enter hourly rate of the worker ($00.00): "))
salary = hours * rate
if(hours<=40):
    print("Salary is : ", salary)
elif(hours>40):
    extratime = hours - 40
    extratime_rate = extratime * rate * 0.5
    salary = salary + extratime_rate
    print("Salary is :", salary)
else:
    print("invalid entry")

# The factorial of a non negative integer n is written n! (pronounced “n factorial”) and is defined as follows:
num = int(input("Enter a number: "))
factorial = 1
if(num < 0):
   print("Invalid Entry")
elif(num == 0):
   print("The factorial of 0 is 1")
else:
   for x in range(1, num+1):
       factorial = factorial*x
   print("The factorial of", num, "is", factorial)
