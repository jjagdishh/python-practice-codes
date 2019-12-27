# list1=['jagdish','abnish','vikas','farrukh','rathish','vikas','farrukh']
#
# list1[0]='Ramesh' # To update a list
# print (list1)
#
# list1.append('jagdish') # to append a new value in list
# print(list1)
#
# list1.remove('vikas')  # To remove an value from a list without knowing its index position
# # Note: if we have multiple similar values in the list delete/remove command will remove only the first value from the list
# print(list1)
#
# del list1[0]   # To remove a value with its index number
# print(list1)
#
# print (list1[-1]) # To print the last value from a list
# print (list1.index('farrukh')) # To search for a Index number of a Value (it will search for the first value)
#
# FOR loop to get total items in the list
list2 = ['Mango', 'Car', "Apple", "Truck",'Bus', 'Car']

#Option-1 -----------------------------------------------------------------------------------
all_value_in_list = len(list2)
for steps in range(all_value_in_list):
    print (list2[steps])

print ("------"*30)

#Option-2 -----------------------------------------------------------------------------------
for name in list2:
    print (name)

print ("------"*30)

# If you need an output with shorting the values alphabetically use this method ------------
list2.sort()

for name in list2:
    print (name)
    
    
    