#The formulas for calculating BMI are
#BMI = (weightInKilograms) / (heightInMeters * heightInMeters)
#Create a BMI calculator application that reads the user‟s weight in kilograms and height
#in meters, then calculates and displays the user‟s body mass index. Also, the application
#should display the following information from the Department of Health and Human
#Services/National Institutes of Health so the user can evaluate his/her BMI:

weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

BmI = weight / (height * height)

print("BMI: ", BmI)
if(BmI < 18.5):
    print("Underweight")
elif(BmI>=18.5 and BmI<=24.9):
    print("Normal")
elif(BmI>=25 and BmI<=29.9):
    print("Overweight")
else:
    print("Obese")