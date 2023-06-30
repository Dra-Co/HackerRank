#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = list(filter(lambda x: x != " ", s))
    s2 = []
    r = math.ceil(math.sqrt(len(s)))
    for i in range(0,r):
        while i < len(s):
            s2.append(s[i])
            i += r
        s2.append(" ")
    return "".join(s2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
