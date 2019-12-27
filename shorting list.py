
list= ["1", "4", "2", "9", "7","10"] # we have a like string
# to short we can use short function like below
list.sort()
print(list)
# Output: ['1', '10', '2', '4', '7', '9']
# So it will short the strings but like that not as integer numbers
# to short the number list in correct order we can do like this
list1= ["1", "4", "2", "9", "7","10"]
list1= [int(i) for i in list1]
list1.sort()
print (list1)

