# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
x, y = input().split()
print(*["".join(i) for i in sorted(list(permutations(x, int(y))))], sep="\n")
