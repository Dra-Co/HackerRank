# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
x, y = map(int, input().split())
arr = []
for _ in range(x): 
    arr.append(list(map(lambda x: int(x)**2, input().split()))[1:])
print(max([sum(i)%y for i in set(product(*arr))]))
