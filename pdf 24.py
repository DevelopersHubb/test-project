# Write a program to find the binary equivalent of the entered number., i.e. binary
# equivalent of 170 is 10101010

number = int(input("Enter Number: "))
list1 = number
conv = 0
n = 0
while(list1 > 0):
    conv = ((list1 % 2) * (10 ** n)) + conv
    list1 = int(list1/2)
    n += 1

print("After conversion: ", conv)

# Write a program to find the range of a set of numbers. Range is the difference between
# the smallest and biggest number in the list. You are not allowed to use built-in range()
# function.

list1 = [4,2,5,7,14,16,21,25,9]
bigNum = 0
small_num = list1[0]
for x in range(len(list1)):
    value = list1[x]
    if(value >= bigNum):
      bigNum = value
    if(value <= small_num):
      small_num = value
ran = bigNum - small_num
print("------------------------Output------------------------")
print ("Range in the given list is", ran)

# Write a program to generate all combinations of 1, 2 and 3 using for loop.
for x in range(1, 4):
   for y in range(1, 4):
      for z in range(1, 4):
        print([x]+[y]+[z])