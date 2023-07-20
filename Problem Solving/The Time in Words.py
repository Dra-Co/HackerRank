#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    num = {1:'one minute', 2:'two minutes', 3:'three minutes', 4:'four minutes', 5:'five minutes', 6:'six minutes', 7:'seven minutes', 8:'eight minutes', 9:'nine minutes', 10:'ten minutes', 11:'eleven minutes', 12:'twelve minutes', 13:'thirteen minutes', 14:'fourteen minutes', 15:'quarter', 16:'sixteen minutes', 17:'seventeen minutes', 18:'eighteen minutes', 19:'nineteen minutes', 20:'twenty minutes', 21:'twenty one minutes', 22:'twenty two minutes', 23:'twenty three minutes', 24:'twenty four minutes', 25:'twenty five minutes', 26:'twenty six minutes', 27:'twenty seven minutes', 28:'twenty eight minutes', 29:'twenty nine minutes', 30:'half'}
    hours = {1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'egiht', 9:'nine', 10:'ten', 11:'eleven', 12: 'twelve'}
    return f"{hours[h]} o' clock" if m == 0 else f"{num[60-m]} to {hours[1 if h == 12 else h+1]}" if m > 30 else f"{num[m]} past {hours[h]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
