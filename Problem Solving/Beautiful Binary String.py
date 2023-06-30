#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Write your code here
    res = 0
    while b.find("010") != -1:
        b = b[:b.find("010")+2] + "1" + b[b.find("010")+3:] if b.find("010")+3 < len(b) and b[b.find("010")+3] == "1" else b[:b.find("010")+1] + "0" + b[b.find("010")+2:]
        res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
