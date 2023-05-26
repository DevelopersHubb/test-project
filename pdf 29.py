#   1
#  2 3
# 4 5 6
#7 8 9 10

size = 4
num = 1
m = size-1
for x in range(0, size):
    for y in range(0, m):
        print(end='  ')
    m -= 1
    for z in range(0, x+1):
        print(num, " ", end=' ')
        num += 1
    print(" ")