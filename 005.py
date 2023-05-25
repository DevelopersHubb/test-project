#6.	Write a Python program to count the number 4 in a given list.

list1 = [1,4,25,43,47,6,8]
count = 0
for x in range(0,len(list1)):
    n = str(list[x])
    for y in range(0, len(n)):
        if(y == 4):
            count += 1
            print (count)
        # print("This is the 4th Number in the list: ", list1[x])
print(count)

# count number of 4's in the list