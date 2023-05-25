#8.	Print the following patterns using loop :
"""
*
**
***
****
"""

for x in range(0, 4):
    for y in range(0, x+1):
        print("*", end='')
    print("\r")
   