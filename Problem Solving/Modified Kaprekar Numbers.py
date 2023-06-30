#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    res = []
    for i in range(p, q+1):
        temp = str(i**2)
        if i == 1 or (len(temp) > 1 and int(temp[len(temp)//2:])+int(temp[0:len(temp)//2]) == i):
            res.append(i)
    print(" ".join(list(map(str, res))))if res else print("INVALID RANGE")
        

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
