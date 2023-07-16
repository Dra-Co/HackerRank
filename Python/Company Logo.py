#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    print(*[" ".join(map(str, i)) for i in sorted(Counter(s).most_common(3), key=lambda x: x[1], reverse=True)], sep="\n")
    
