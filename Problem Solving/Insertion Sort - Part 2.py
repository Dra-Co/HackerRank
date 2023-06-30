#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        temp = arr[i]
        while arr[i] < arr[i-1] and i > 0:
            arr[i] = arr[i-1]
            arr[i-1] = temp
            i -= 1
        print(str(arr)[1:-1].replace(",", ""))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
