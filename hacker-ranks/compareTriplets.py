import math
import os
import random
import re
import sys
def compareTriplets(a,b):
    a1 = 0
    b1 = 0
    for i , element in enumerate(a):
        if element > b[i]:
            a1 += 1
        elif element == b[i]:
            pass
        elif element < b[i]:
            b1 += 1
    return a1,b1

a = [5,6,7]
b = [3,6,10]
result = compareTriplets(a,b)