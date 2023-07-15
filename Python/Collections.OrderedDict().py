# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
items = OrderedDict()
n = int(input())
for i in range(n):
    a, b = input().rsplit(maxsplit=1)
    if a in items:
        items[a] += int(b)
    else:
        items[a] = int(b)
for i,v in items.items():
    print(i, v)
