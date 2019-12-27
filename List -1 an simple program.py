# We are capturing a name list from user input here and storing the names in a list called "list"
# using a while loop for name
# user can type the name in any combination of letter case, but we are converting the values into upper case
# so that we can easily handel the list
# Then we are shorting the list and printing the result using a for loop


list=[]
name= " "

while name != "done".upper():
    name = (input("Please Enter the name of the guests 'when done Enter 'done': ").upper())
    list.append(name)
    if name == "done".upper():
        list.remove("done".upper())

list.sort()
for guests in list:
    print ("You have entered Name as :",guests)

