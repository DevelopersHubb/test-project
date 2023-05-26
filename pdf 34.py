# *
# ***
# *****
# *******
# *********
# *******
# *****
# ***
# *

rows = 10
for x in range(0, rows):
    if(x % 2 == 0):
        for y in range(0, x+1):
            print("*", end='')
        print("\r")

for x in range(rows-1, 0, -1):
    if(x % 2 == 0):
        for y in range(0, x-1):
            print("*", end='')
        print("\r")
