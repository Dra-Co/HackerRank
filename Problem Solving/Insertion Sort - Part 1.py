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
    x = arr[n-1]
    k = n-2
    while arr[k] > x and k >= 0:
        arr[k+1] = arr[k]
        print(' '.join(map(str, arr)))
        k -= 1
    arr[k+1] = x
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
