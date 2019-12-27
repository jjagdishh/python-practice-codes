import os
hostname = "192.168.43.121" #example
response = os.system("ping -n 4 " + hostname)

#and then check the response...
if response == 0:
  print (hostname, 'is up!')
else:
  print (hostname, 'is down!')