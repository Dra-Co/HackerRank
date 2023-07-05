#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    res = "NO"
    for i in range(1, len(s)//2+1):
        x = y = s[:i]
        num = int(y)
        while len(s) > len(x):
            num += 1
            x += str(num)
        if x == s:
            res = "YES " + str(y)
    print(res)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
