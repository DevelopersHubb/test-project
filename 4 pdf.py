# #Write a program that takes the marks obtained by a student in five different subjects as
# #input through the keyboard, then find out the total marks and percentage marks obtained
# #by the student in each subject. Assume that the maximum marks that can be obtained by a
# #student in each subject is 100.

# a = int(input("Enter Marks of 1st Subject: "))/ 100 * 100
# b = int(input("Enter Marks of 2nd Subject: "))/ 100 * 100 
# c = int(input("Enter Marks of 3rd Subject: "))/ 100 * 100
# d = int(input("Enter Marks of 4th Subject: "))/ 100 * 100
# e = int(input("Enter Marks of 5th Subject: "))/ 100 * 100

# percenta = totalMarks / 5

# print("Total Marks: ", totalMarks)
# print("Percentage: ", percenta)
# print("Percentage in each subject are :", "\nSubject 1:" , a , "\nSubject 2:" , b ,"\nSubject 3:", c ,"\nSubject 4:" , d , "\nSubject 5:" , e)

# perform using loop ----------------------

add = 0
total_marks = 100
print("Enter marks of 5 subjects:")
for x in range(1,6):
    marks = float(input("Enter marks:"))
    add = marks + add
    print("Percentage of Subject", x , ":", marks/total_marks * 100)

print("Total Marks =",add)
print("Total Percentage =", add/5)

# done


#Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a
#program to convert this temperature into Centigrade degrees

faren = float(input("Enter Temperature : "))
c = (faren-32)*5/9
print("Temperature in Centigrade : ", "%.2f" % c)

# print output for 2 decimal points