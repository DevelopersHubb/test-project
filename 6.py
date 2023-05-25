# vi.	Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. 
# Both arrays will be length 1 or more. 

arr1 = [2,2,3]
arr2 = [2,3,2]
# count = 0

if(arr1[0] == arr2[0] or arr1[-1] == arr2[-1]):
    print("True")

# vii.	Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values,
# it does not count towards the sum. 
# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

data1 = [5,1,3]
count = 0

for items in range(0, len(data1)):
    if(data1[0] != data1[1] and data1[0] != data1[2] and data1[1] != data1[2]):
        count = count + data1[items]
        print(count)
        continue
    if(data1[0] == data1[1]):
        if(data1[0] == data1[2]):
            print(count)
            break
        count = count + data1[2]
        print(count)
        break
    elif(data1[0] == data1[2]):
        count = count + data1[1]
        print(count)
        break
    else:
        count = count + data1[0]
        print(count)
        break