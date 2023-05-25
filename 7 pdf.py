#If a five-digit number is input through the keyboard, write a program to calculate the sum
#of its digits. (Hint: Use the modulus operator „%‟ to split the digits).

add = 0
val = 0
num1 = input("Enter a Number: ")

for x in range(0,len(num1)):
    if (len(num1) == 5):
        val = int(num1[x])
        add = add + val
    else:
        print("Invalid Entry!!!")
        break
print("Sum = ", add)