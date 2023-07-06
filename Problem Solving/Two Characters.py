#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    lst = list(set(s))
    m = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            alt = "".join(list(filter(lambda x: x == lst[i] or x == lst[j], s)))
            if alt == (alt[:2] * (len(alt)//2) if len(alt) % 2 == 0 else alt[:2] * (len(alt)//2) + alt[0]) and len(alt) > m:
                m = len(alt)
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
