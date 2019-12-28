#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = int(s[:2])
    print(hour)
    if "AM" in s:
        if hour == 12:
           hour = "00"
           s = hour+s[2:-2]
           return s
        else:
            return s.replace("AM","")
    else:
        if hour == 12:
            return s.replace("PM","")
        else:
            hour+=12
            return str(hour) + s[2:-2]





if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
