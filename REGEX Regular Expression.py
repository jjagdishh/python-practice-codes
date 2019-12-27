import re
file1 = "D:/userdata/jmathpal/Desktop/1.txt"
open_file1 = open(file1)
file1_data = open_file1.read()
x = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",file1_data)
print (x[0])


'''
# .     --> Any Character expect new line 
# \d    --> Digits (0-9)
# \D    --> Not a Digit (0-9)
# \w    --> Word Character (a-z, A-Z, 0-9, _)
# \W    --> Not an Word Character 
# \s    --> Whitespace (Space, Tab, Newline)
# \S    --> Not Whitespace (Space, Tab, Newline)
# \b    --> Word Boundary  (word boundary is Indicated by Whitespace or non alphanumeric character)
# \B    --> Not a Word Boundary
# ^     --> Binging of a String
# $     --> End of a String
# []    --> Matches character in brackets 
# [^]    --> Matches character not in brackets 

'''