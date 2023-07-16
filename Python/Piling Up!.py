# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
for _ in range(n):
    _ = input()
    d = deque(map(int, input().split()))
    temp = max(d)
    while len(d) != 0:
        if d[0] <= temp and d[-1] <= d[0]:
            temp = d[0]
            d.pop()
        elif d[-1] <= temp and d[0] <= d[-1]:
            temp = d[-1]
            d.popleft()
        else:
            break
    print("No") if len(d) else print("Yes")
