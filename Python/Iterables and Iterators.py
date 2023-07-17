# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
_ = input()
s = list(input().split())
l = int(input())
x = list(combinations(s, l))
print(len(list(filter(lambda x: 'a' in x, x)))/len(x))
