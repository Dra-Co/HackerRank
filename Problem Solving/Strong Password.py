#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    q = [True] * 4
    for i in password:
        if i.isupper():
            q[0] = False
        elif i.islower():
            q[1] = False
        elif i.isnumeric():
            q[2] = False
        elif not i.isalnum():
            q[3] = False
    if n+sum(q) > 5:
        return sum(q)
    else:
        return 6-n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
