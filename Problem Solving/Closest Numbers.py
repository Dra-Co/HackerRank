#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr = sorted(arr)
    res = []; m = abs(arr[0]-arr[1])
    for i in range(1, len(arr)-1):
        if abs(arr[i+1]-arr[i]) <= m:
            if abs(arr[i+1]-arr[i]) < m:
                m = abs(arr[i+1]-arr[i])
                del res[:]
            res.extend([arr[i], arr[i+1]])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
