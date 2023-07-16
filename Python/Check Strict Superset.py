# Enter your code here. Read input from STDIN. Print output to STDOUT
n = set(input().split())
res = True
for _ in range(int(input())):
    res = n.issuperset(set(input().split()))
    if not res:
        break
print(res)
