# With a given integer number n provided by the user, write a program to generate a dictionary
# that contains {i: i*i} as its key:value pair such that all the integer numbers between 1
# and n are included). At the end, your program should print the dictionary. Suppose the
# following input is supplied to the program:

num = int(input("Enter a number: "))
dict1 = dict()
for x in range(1, num+1):
    dict1[x] = x*x
print(dict1) 


# Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically. Suppose the
# following input is supplied to the program:

phrase = input("Input words: ")
phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))