# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

start = int(input())
s = Counter(map(int, input().split()))
n = int(input())
res = 0
for i in range(n):
    x, y = map(int, input().split())
    if s[x] > 0:
        s[x] -= 1
        res += y
print(res)


