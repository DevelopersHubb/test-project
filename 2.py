#2.	Write a function which should add the two vowels in the arrays and generate third array

# str1 = "my name is salman"
# str2 = "what's yours"
# str3 = ""
# temp = 0

# print("Vowels in 1st Array:")

# for x in range(0, len(str1)):
#     temp = str1[x]
#     if(temp == 'a' or temp == 'e' or temp == 'i' or temp == 'o' or temp == 'u'):
#         str3 += temp
#         print(temp)

# print("Vowels in 2nd Array:")

# for y in range(0, len(str2)):
#     temp = str2[y]
#     if(temp == 'a' or temp == 'e' or temp == 'i' or temp == 'o' or temp == 'u'):
#         str3 += temp
#         print(temp)

# print("Vowels in 3rd Array:")
# print(str3)

# perform using array-----------------------------
# remove range and temp variable---------------------
# create an array of vovels and use that array to compare------

arr1 = "my name is salman"
arr2 = "what's yours"
arr3 = [arr1 + arr2]
arr4 = []
# print (arr3)
arr_v = ['a','e','i','o','u']
count = 0
# print("Vowels in 1st Array:")
for x in range(0, len(arr1)):
    for y in range(0,len(arr_v)):
        if(arr1[x] == arr_v[y]):
            arr4 += arr1[x]
            # arr4.insert[arr1[x]]
            count += 1
# print(arr4)

print("Vowels in 3rd Array:")
for x in range(0, len(arr2)):
    for y in range(0,len(arr_v)):
        if(arr2[x] == arr_v[y]):
            arr4 += arr2[x]
            # arr4.insert[arr1[x]]
            count += 1
print(arr4)
print(count)

# for x in range(len(arr)):
#     array.append(str(input()))
# print("1st Array contains:", array)    
