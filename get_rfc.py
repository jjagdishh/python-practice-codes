import sys, urllib.request
import re, os

try:
    rfc_number = int(input("please input an RFC Number:"))
except:
    print("Must supply a RFC Number")
    sys.exit(0)
while True:
    template = 'https://www.rfc-editor.org/rfc/rfc{}.txt'
    url = template.format(rfc_number)
    try:
       rfc_raw = urllib.request.urlopen(url).read()
       rfc = rfc_raw.decode()
       path = os.environ["HOMEPATH"]+"\Desktop\\"
       file = open(path+'rfc{}.txt'.format(rfc_number),'w')
       write = file.write(rfc)
       file.close()
       print("RFC has been saved at your Desktop")
       sys.exit(0)
    except(Exception):
        print("Page not found error, Given RFC number not available")
    sys.exit(0)