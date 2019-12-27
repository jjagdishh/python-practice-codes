import re
import pandas as pd
file1 = "C:/Users/jmathpal/Desktop/RegulerEx/local0log.0"
open_file1 = open(file1)
file1_data = open_file1.read()
#a = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",file1_data)
b = re.findall("result code ...",file1_data)
for i in b:
    print(i)