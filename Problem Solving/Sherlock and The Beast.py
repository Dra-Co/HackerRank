#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Write your code here
    x = n//3; y = 0
    while (n - 3*x) % 5 != 0 and x > 0:
        x -= 1
    if (n-x*3) % 5 == 0:
        y = (n-x*3) // 5
    print("555"*x+"33333"*y) if x or y else print(-1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
