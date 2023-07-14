# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
a, b = map(int, input().split())
for i in range(1, a+1):
    d[input()].append(i)
for i in range(b):
    res = input()
    print(*d[res]) if d[res] else print(-1) 
