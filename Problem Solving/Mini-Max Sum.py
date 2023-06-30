#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    def sum(a, b):
        return a + b;
    
    print(functools.reduce(sum, arr[:len(arr)-1]),functools.reduce(sum, arr[1:]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
