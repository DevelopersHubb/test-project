#For e.g. The given string is 1234566
#The subsequences divisible by 6 are 12, 24, 36, 36, 6, 6, 66
#Hence the answer should be 7

str1 = "1234566"
count = 0
c = ""
#value = 0
for x in range(0,len(str1)):
  if (int(str1[x]) % 6 == 0):
    count += 1
  for y in range(x+1, len(str1)):
    c = (str1[x] + str1[y])
    if (int(c) % 6 == 0):
      count += 1
print(count)