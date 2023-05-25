#v.	Given an array of ints, return True if .. 1, 2, 3,.. appears in the array somewhere. 

arr1 = [2,1,2,3,4,5,5,2,1,2,3]
for x in range(0, len(arr1)):
    if(arr1[x] == 1):
        if(x+1 >= len(arr1)):
            continue
        if (arr1[x+1] ==2):
            if(x+2 >= len(arr1)):
                continue
            if(arr1[x+2] ==3):
                if(x+2 >= len(arr1)):
                    break
                print("True")
            else:
                print("False")