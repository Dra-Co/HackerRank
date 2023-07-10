#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks = sorted(sticks, reverse=True)
    for x in range(len(sticks)):
        for y in range(x+1, len(sticks)):
            for z in range(y+1, len(sticks)):
                if sticks[x] + sticks[y] > sticks [z] and sticks[y] + sticks[z] > sticks[x] and sticks[z] + sticks[x] > sticks[y]:
                    return [sticks[z], sticks[y], sticks[x]]
    return [-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
