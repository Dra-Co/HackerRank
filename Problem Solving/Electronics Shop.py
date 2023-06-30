#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards = sorted(keyboards, reverse = True)
    drives = sorted(drives)
    n = maxi = 0
    if keyboards[-1] + drives[0] > b: return -1
    for i in drives:
        for j in range(0, len(keyboards)):
            if i + keyboards[j] <= b and i + keyboards[j] > maxi:
                maxi = i + keyboards[j]
                break
    return maxi
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
