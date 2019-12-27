import datetime
#############################DATE##############################################
today=datetime.date.today()
'''print (today)
print (today.year)
print (today.month)
print (today.day)
print (today.strftime("%d %b %y")) # %d= date %b=Month %y=year (%m is used for minute for time)
# for more strftime codes follow : http://strftime.org/

# Now we wil see how can we get the exact numbers of years you old are from your date of birth
userInput = input("Please enter your DOB in format (dd/mm/yyyy/)")
dob = datetime.datetime.strptime(userInput, '%d/%m/%Y').date() #%d/%m/%Y is the format in which the function need user input
# Note .date is used to get just only the Date not the time for your DOB
print (dob)
print (today)
days= (today - dob)
years= (days/365)
print ("You are %r years old" %years.days) # .days will return the exact number of years from subtraction'''

#################################TIME########################################
time=datetime.datetime.now()
print (time)
print (time.time())
print (time.hour)
print (time.minute)
print (time.second)
print (time.strftime('%H %M %S'))  # for more strftime codes follow : http://strftime.org/
