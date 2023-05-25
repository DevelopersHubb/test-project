# 3.	Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

def func(Num1):
    output = Num1 - 17
    if Num1 >= 17:
        output = output * 2
    return output 

print(func(32))