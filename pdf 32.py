#(A)        (B)          (C)         (D)
#*       **********    **********     *
#**       *********    *********     **
#***       ********    ********     ***
#****       *******    *******     ****
#*****       ******    ******     *****
#******       *****    *****     ******
#*******       ****    ****     *******
#********       ***    ***     ********
#*********       **    **     *********
#**********       *    *     **********
# (A)
rows = 10
for x in range(0, rows):
    for x in range(0, x+1):
        print("*", end=' ')
    print("\r")
print("\n")
# (B)
rows = 10
for x in range(rows+1, 0, -1):
    for y in range(0, x-1):
        print("*", end=' ')
    print(" ")
    rows -= 1

print("\n")
# (C)
rows = 10
for x in range(1, rows + 1):
    for y in range(1, rows + 1):
        if(y < x):
            print(" ", end = ' ')
        else:
            print("*", end = ' ')
    print()
print("\n")
# (D)
rows = 10
k = 2 * rows - 2
for x in range(0, rows):
    for y in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, x+1):
        print("* ", end="")
    print("")