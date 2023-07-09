#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
    arr = dict(enumerate(arr))
    n = {j:i for i, j in arr.items()}
    for i in range(len(arr)):
        if arr[i] != len(arr)-i and k:
            n[arr[i]] = n[len(arr)-i]
            arr[n[len(arr)-i]] = arr[i]
            arr[i] = len(arr)-i
            k -= 1
    return list(arr.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
