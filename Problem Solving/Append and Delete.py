#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    x = 0
    for i in range(0, min(len(s), len(t))):
        if s[i] == t[i]: x+= 1
        else: break
    if k - (len(s) -x) >= len(t)-x and ((len(t)-x)%2 == (k - (len(s) -x))%2 or (k - (len(s) -x)) - x >= len(t)):
        return "Yes"
    return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
