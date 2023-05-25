#A)   
#**********
#**********
#**********
#**********
print("-----------------------------------------------------")
for x in range(0,4):
    for y in range(0, 10):
        print("*", end= '')
    print("\r")

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

print("-----------------------------------------------------")
for x in range(1,6):
    for y in range(1, x+1):
        print(y," ", end= '')
    print("\r")

#1 2 3 4 5 6 7 8 9 10 
#2 4 6 8 10 12 14 16 18 20
#3 6 9 12 15 18 21 24 27 30 
#4 8 12 16 20 24 28 32 36 40
#5 10 15 20 25 30 35 40 45 50

num1 = 1
val = 6
col = 11
print("-----------------------------------------------------")
for x in range(num1,val):
    #val = val * x
    for y in range(1, col):
        print(y*num1," ", end= '')
    print("\r")
    num1 =  num1 + 1 

#2. Write a Python program to multiplies all the items in a list.  

list1 = [2, 4, 1, 5, 8]
multi = list1[0]
print("-----------------------------------------------------")

for x in range(1,len(list1)):
    multi = multi * list1[x]

print("Answer is:",multi)

#3. Write a Python program to get the smallest number from a list.

list1 = [4,5,7,14,16,21,25,9]
small_num = list1[0]
print("-----------------------------------------------------")
for x in range(1, len(list1)):
    value = list1[x]
   #small_num = list1[0]  
    if(value <= small_num):
        small_num = value 
print ("Smallest Number in the given list is", small_num)  

#4. Write a Python program to remove duplicates from a list

print("-----------------------------------------------------")
list1 = [4,5,7,14,16,21,4,5,7,7,9,25,9]
print("Before removing:", list1)

remve = [*set(list1)]
print("After removing all the duplications:", remve)

#5. Write a Python program to clone or copy a list.

print("-----------------------------------------------------")
list1 = [4,"Many",5,7,14,16,21,4,5,7,7,9,25,9]

cpy = list1.copy()
print(cpy)
print(list1)

# there is no effect on the original list
# check if original array effect after copying---------------------


#6. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("-----------------------------------------------------")

count = 0
pos = 0
n=0
for x in range(n,len(list1)):
    if (x == pos):
        # list1.pop(x)
        # new_list.append(list1[x])
        del list1[x]
        count += 1
        if(count == 1):
            pos += 2
        n=0
# print(*list1)
# print(list1)
remve = [*set(list1)]
print("After removing all the duplications:", remve)

# perform remove not skip 