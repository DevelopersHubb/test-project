# Given an input n, count the total number of digit 1 appearing in all nonnegative
# integers less than or equal to n.

n = 13
count = 0
    
for x in range(1, n+1):
    str1 = str(x)
    count += str1.count("1")
    #print(str1)
    
print(count)