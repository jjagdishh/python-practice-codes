from datetime import date
import calendar
my_date = date.today()
day=(calendar.day_name[my_date.weekday()])
date = date.today()

month=(my_date.month)
if month == 1:
    m= ('January')
elif month == 2:
    m= ('February')
elif month == 3:
    m= ('March')
elif month == 4:
    m= ('April')
elif month ==5:
    m= ("May")
elif month == 6:
    m= ('June')
elif month == 7:
    m= ('July')
elif month == 8:
    m=  ('August')
elif month == 9:
    m=  ('September')
elif month == 10:
    m= ('October')
elif month == 11:
    m= ('November')
elif month == 12:
    m= ('December')

print('It\'s %s %r' %(m,day))
print(my_date)
print('')
print ("Hi Welcome to my page! I can calculate you BMI ")
print('')
print('Please input your data here')
name= input("what is your Name ?")
age= int(input("what is your Age?"))
weight= int(input("what is your Weight?"))
hight= int(input("what is your height in CM"))
print('')
print('')
print("Okey %r So you are %r years old and %r CM tall and your Weight is %r" %(name,age,hight,weight))
print('')
print('')
hight1=hight*hight
weight1= (weight*10000)
bmi=round(weight1/hight1)
print("%r your body mass index is %r" %(name,bmi))
