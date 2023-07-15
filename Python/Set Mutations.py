# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s = set(input().split())
for _ in range(int(input())):
    m, *a = input().split()
    getattr(s, m)(set(input().split()))
print(sum(map(int, s)))
