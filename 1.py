#i.	Write a program which should count Vowels in the strings and return vowels in reverse order. 

str1 = "we have to find vowels in the given string"
reverse_string = str1[::-1]
print("In Revese Order :", reverse_string)
count = 0
temp = 0
print("Vowels present in the given string are :")

# for x in range(len(str1), 0, -1):
#   temp = str1[x-1]
#   if(temp == 'a' or temp == 'e' or temp == 'i' or temp == 'o' or temp == 'u'):
#     count += 1
#     rev_value = temp
#     print(rev_value)

for x in range(0, len(reverse_string)):
  if(reverse_string[x] == 'a' or reverse_string[x] == 'e' or reverse_string[x] == 'i' or reverse_string[x] == 'o' or reverse_string[x] == 'u'):
    count += 1
    print(reverse_string[x])
print("\nTheir count is", count)

# Remove Extra variables and Range

# done