#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    if b.replace("_","") and min(Counter(b.replace("_","")).values()) == 1:
        return "NO"
    elif b.find("_") == -1:
        temp = [b[0]]
        for i in range(len(b)-1):
            if b[i] != b[i+1] and b[i+1] not in temp:
                temp.append(b[i+1])
            elif b[i] != b[i+1] and b[i+1] in temp:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
