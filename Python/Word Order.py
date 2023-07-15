# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
q = [input() for _ in range(int(input()))]
res = Counter(q)
print(len(res))
print(*res.values())
