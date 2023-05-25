#x.	Write a the function LongestWord (sen) take the sen parameter being passed and return the largest word in the string. 
# If there are two or more words that are the same length, return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty.

str1 = "i live city lahore pakistan"
count = 0
c=0
temp = 0
for x in range(0, len(str1),temp+1):
    for y in range(x, len(str1)):
        if(str(str1[y]) != " "):
            count += 1
        else:    
            break
        if(count>=temp):
            temp = count    
    count = 0
print(temp)

# perform using split(" ")