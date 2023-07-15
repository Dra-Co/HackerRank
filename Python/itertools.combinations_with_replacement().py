# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
n = input().split()
print(*sorted(["".join(sorted(i)) for i in combinations_with_replacement(n[0],int(n[1]))]), sep="\n")

