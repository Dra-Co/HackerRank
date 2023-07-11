#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # Write your code here
    return "Second"if set(s) == {1} and len(s) % 2 == 1 else "First" if functools.reduce(lambda x,y: x ^ y,s) or (set(s) == {1}and len(s) % 2 == 0) else "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
