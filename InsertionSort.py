#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    temp = arr[n-1]
    for i in range(n-1):
        if arr[n-i-2]>temp:
            arr[n-i-1] = arr[n-i-2]
            print(*arr)
        elif arr[n-i-2]<temp:
            arr[n-i-1]=temp
            print(*arr)
            break
        if arr[0] == arr[n-i-2]:
            arr[0] = temp
            print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
