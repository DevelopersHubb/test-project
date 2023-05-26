#A library charges a fine for every book returned late. For first5 days, the fine is 50 paise,
#for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book
#after 30days your membership will be cancelled. Write a program to accept the number
#of days the member is late to return the book and display the fine or the appropriate
#message.
days = int(input("Enter days book returned after due date: "))

if (days <= 5):
    fine = 50
    print("Fine:", fine, "paise")
elif (days > 5 and days < 11):
    fine = 1
    print("Fine:", fine, "ruppee")
elif (days > 10):
    fine = 5
    print("Fine:", fine, "ruppee")
elif (days > 30):
    print("Your Membership has been cancelled.")

# A university has the following rules for a student to qualify for a degree with A as the
# main subject and B as the subsidiary subject:
# (a) He should get 55 percent or more in A and 45 percent or more in B.
# (b) If he gets than 55 percent in A he should get 55 percent or more in B. However, he
# should get at least 45 percent in A.
# (c) If he gets less than 45 percent in B and 65 percent or more in A he can reappear in an
# examination in B to qualify.
# (d) In all other cases he is declared to have failed.

a = float(input("Enter Percent in A: "))
b = float(input("Enter percent in B: "))

if(a >= 55 and b >= 45):
    print("Student is passed")
elif(a >= 45 and a < 55 and b >= 55):
    print("Student is passed")
elif(b < 45 and a >= 65):
    print("Student is allowed to reappear in exam B to qualify")
else:
    print("Student is failed")