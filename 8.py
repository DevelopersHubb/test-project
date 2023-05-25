#viii.	Given a string you are provided with the possible operations.
#We can group the adjacent substrings, for e.g ABCABCBC can be compressed as 
#2ABC1BC or 1ABCA2BC

str1 = "ABCABCBC"
c = []
count = 0

# for x in str1:
#     if any((match := substring) in str1 for substring in c):
#         print(match)
#         c[x] = match
#         x += 1
#     else:
#         print("It doesnot contains any of it's string")

# for x in range(0, len(str1)):
#     for y in range(x+1, len(str1)):
#         for z in range(y+1, len(str1)):
#             c = str1[x] + str1[y] + str1[z]
#             if(c == 'ABC'):
#                 count += 1
# print(count)
for x in range(0,len(str1)):
    if str1[x] in c:
        # c.append(str1[x])
        count +=1
        print(count)
