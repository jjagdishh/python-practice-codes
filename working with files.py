# In this demo we will see different method to create a new file in different methods and how you can access them

# to Create a file
file= "Demo.text"
# Note if you do not give the exact path for your file it will be created in the default folder of that project
permission= "r" # Always use the permission what you required at that time
# w= write
# r= read
# a= append
myfile= open(file,permission)
# Now File has been created we will write something in our file
myfile.write("hey this is a demo text file \n")

#Now we will append some text in the file

myfile.write("we are appending some text her \n ")
# Note make sure the file permission is set to "w" while appending something in a file else it will overwrite the existing information


# Now lets write an CSV file. A Comma is used to separate the lines in the csv file

myCsv= open("DemoCsv.csv",'w')
myCsv.write("Jagdish,20 \n")
myCsv.write("Abnish,20 \n")

# to read a file
print(myfile.read())

myfile.close()
myCsv.close()

# If you need to delete an file from your system

import os
os.remove('Demo.text')
os.remove('DemoCsv.csv')


# For Loop to read a text file and its Word

myfile = open("Demo.text",'r')
myfile.readline()

for currentline in myfile:
    print(currentline)
    for currentword in currentline:
        print (currentword)
