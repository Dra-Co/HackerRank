#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    w = list(w)
    p, x, y = False, -1, 0
    for i in range(len(w)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if w[i] > w[j] and j > x:
                x, y, p = j, i, True
    w[x], w[y] = w[y], w[x]
    return ''.join(w[:x+1]+sorted(w[x+1:])) if p else 'no answer'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
