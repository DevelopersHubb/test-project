#Given an input n, count the total number of digit 1 appearing in all nonnegative
#integers less than or equal to n.
#For example:
#Given n = 13,
#Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

list1 = [1,10,11,12,13]
count = 0
temp = []
for x in range(0,len(list1)):
    temp = list1[x]
    if(temp == 1 or temp == 0):
        count = count + 1
        print(count)

# using this example by inputing an integer
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.