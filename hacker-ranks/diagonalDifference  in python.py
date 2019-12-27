matrix =[[11, 2, 4],
        [4, 3, 6],
        [10, 8, 12]]

def diagonalDiff(matrix):
    la = []
    ra = []
    for i in range(len(matrix)):
        la.append(matrix[i][i])
    for i in range(len(matrix)):
        ra.append(matrix[len(matrix)-1-i][i])
    print(la)
    print(ra)
    return sum(la) - sum(ra)
print(diagonalDiff(matrix))


'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    la= []
    ra= []
    for i in range (len(arr)):
        la.append(arr[i][i])
    for i in range (len(arr)):
        ra.append(arr[len(arr)-1-i][i])
    return abs(sum(la) - sum(ra))
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
