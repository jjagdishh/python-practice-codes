# This is a sample to show the functions in pyton
# we have two list of expensis one for vikas and one for ram. we want to calculate it
# to calculate it we have two options in python one is simple defining for loop for each list and print the total
# second is we can define a function and we can call them may time as we need and we do not have to define for loop each time for each list.

vikas_total_exp=[100,200,500,50,150] # expense list of vikas
ram_total_exp=[200, 300, 400, 300]   # expense list of ram

# First Method!
# uncomment when you want run first method and comment secon method
total=0                       # defining variable total
for item in vikas_total_exp:     # make a for loop for vikas list
    total=total+item             # calculating the total items from list
print("Vikas total expenses = ",total) # printing the output from total 

# same way calculation done for ram expenses 
total=0
for item in ram_total_exp:
    total=total+item
print("Ram's total expenses =",total)

# Second Method
'''def calculating_total(exp):  # defining a function called "calculating_total". exp is the local variable input
    total=0                  # Defining variable total
    for item in exp:         # for loop for expense list "input = exp"
        total=total+item     # calculating the total items from input list
    return total             # returning the total output. Note ! return shoud start from where the for loop start. mind the space
# so our function is ready now we have to calculate the vikas and ram expenses via this function

vikas_total=calculating_total(vikas_total_exp) # calling the function and input the list you want to calculate
ram_total= calculating_total(ram_total_exp)

print (vikas_total) # print the total calculated for the variable
print (ram_total)'''
