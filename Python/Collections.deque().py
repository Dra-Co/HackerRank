# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for _ in range(int(input())):
    m, *a = input().split()
    getattr(d, m)(*a)
print(*d)
