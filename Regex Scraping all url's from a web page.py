import lxml
import requests
import re
from re import *

page = requests.get("https://cloudnfv.wordpress.com/")
p1 = page.text
l = (re.finditer("((https://)|(http://)).*((com)|(/))",p1))
for i in l:
    l1 = (i.group())
    l2 = re.sub("([\"].*)|([\'].*)","",l1)
    print(l2)
