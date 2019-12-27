arr = [-4, 3, -9, 0, 4, 1 ]
def plusMinus(arr):
    pos = 0
    neg = 0
    zero= 0
    arr_len = len(arr)
    for i in arr:
        if i > 0:
            pos+=1
        elif i < 0:
            neg+=1
        elif i ==0:
            zero+=1
    print(pos /arr_len)
    print(neg / arr_len)
    print(zero / arr_len)
plusMinus(arr)

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero= 0
    arr_len = len(arr)
    for i in arr:
        if i > 0:
            pos+=1
        elif i < 0:
            neg+=1
        elif i ==0:
            zero+=1
    print(pos /arr_len)
    print(neg / arr_len)
    print(zero / arr_len)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
'''