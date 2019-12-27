from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import pandas as pd
import csv

page= urlopen('file:///D:/userdata/jmathpal/Desktop/Schedule.cgi') #Query the website and return the html to the variable 'page'
soup = BeautifulSoup(page, 'lxml') #Parse the html in the 'page' variable, and store it in Beautiful Soup format
table=soup.find('table')

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
for row in table.findAll("tr"):
    cells = row.findAll('td')
#    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
#        B.append(cells[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))


df=pd.DataFrame(A,columns=['date'])
#df['Date']=B
df['Day']=C
df['In_Hour']=D
df["A"] = 1
#df['In_Hour-2']=E
df['Out_Hour']=F
df["B"] = 1
#df['Out_Hour-2']=G
#df['Count_In_Hour']=pd.Series()
#df['Count_Out_Hour']=pd.Series()
df.head()

#df.to_csv('D:/userdata/jmathpal/Desktop/Rota_testing.csv') # if you want to save the data in CSV format

######Calculating the data

import pandas as pd
import numpy as np
from collections import defaultdict

#df = pd.read_csv('D:/userdata/jmathpal/Desktop/Rota_testing.csv',skipinitialspace=True) # Import the file if it is saved in local directory

df1=df[df["Day"].isin(['Sat','Sun'])]
df2=df[df["Day"].isin(['Mon','Tue','Wed','Thu','Fri'])]
#For Vikas
df3_v1=(df1.query('In_Hour == ["vikasa"]'))
vikas_week_end_Sat= (df3_v1.In_Hour.count())
df3_v2=(df1.query('Out_Hour == ["vikasa"]'))
vikas_week_end_Sun= (df3_v2.Out_Hour.count())
df3_v3=(df2.query('Out_Hour == ["vikasa"]'))
vikas_week_day_count= (df3_v3.Out_Hour.count())
Vikas_OOH=vikas_week_end_Sat+vikas_week_end_Sun+vikas_week_day_count
print ("Vikas OOH = ",Vikas_OOH)
#For Abnish
df3_A1=(df1.query('In_Hour == ["abnishj"]'))
abnish_week_end_Sat= (df3_A1.In_Hour.count())
df3_A2=(df1.query('Out_Hour == ["abnishj"]'))
abnish_week_end_Sun= (df3_A2.Out_Hour.count())
df3_A3=(df2.query('Out_Hour == ["abnishj"]'))
abnish_week_day_count= (df3_A3.Out_Hour.count())
abnish_OOH=abnish_week_end_Sat+abnish_week_end_Sun+abnish_week_day_count
print ("abnish OOH = ",abnish_OOH)
#For Rathish
df3_R1=(df1.query('In_Hour == ["crathish"]'))
rathish_week_end_Sat= (df3_R1.In_Hour.count())
df3_R2=(df1.query('Out_Hour == ["crathish"]'))
rathish_week_end_Sun= (df3_R2.Out_Hour.count())
df3_R3=(df2.query('Out_Hour == ["crathish"]'))
rathish_week_day_count= (df3_R3.Out_Hour.count())
rathish_OOH=rathish_week_end_Sat+rathish_week_end_Sun+rathish_week_day_count
print ("rathish OOH = ",rathish_OOH)

#For Farrukh
df3_F1=(df1.query('In_Hour == ["fiqbal"]'))
Farrukh_week_end_Sat= (df3_F1.In_Hour.count())
df3_F2=(df1.query('Out_Hour == ["fiqbal"]'))
Farrukh_week_end_Sun= (df3_F2.Out_Hour.count())
df3_F3=(df2.query('Out_Hour == ["fiqbal"]'))
Farrukh_week_day_count= (df3_F3.Out_Hour.count())
Farrukh_OOH=Farrukh_week_end_Sat+Farrukh_week_end_Sun+Farrukh_week_day_count
print ("Farrukh OOH = ",Farrukh_OOH)

#For Jagdish
df3_J1=(df1.query('In_Hour == ["jmathpal"]'))
Jagdish_week_end_Sat= (df3_J1.In_Hour.count())
df3_J2=(df1.query('Out_Hour == ["jmathpal"]'))
Jagdish_week_end_Sun= (df3_J2.Out_Hour.count())
df3_J3=(df2.query('Out_Hour == ["jmathpal"]'))
Jagdish_week_day_count= (df3_J3.Out_Hour.count())
Jagdish_OOH=Jagdish_week_end_Sat+Jagdish_week_end_Sun+Jagdish_week_day_count
print ("Jagdish OOH = ",Jagdish_OOH)


