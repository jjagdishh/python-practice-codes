#Copying one file data to another new file

file1 ="D:/userdata/jmathpal/Desktop/file1.txt" # file 1 path

open_file1 = open(file1) # open file 1
file1_data = open_file1.read() # read file1 contents

open_file2 = open("D:/userdata/jmathpal/Desktop/file3.txt","w+") # create a new file3
open_file2.write(file1_data) # write file1 data into file3

open_file1.close() # close the file
open_file2.close() # Close the file 
