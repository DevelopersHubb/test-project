#2.	Write a Python program to display the first and last colors from the following list.  
#color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green", "sky blue", "yellow" ,"White" ,"Black", "orange"]
outpt = color_list[::len(color_list)-1]
print("Output is: ", outpt)