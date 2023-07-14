# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
s1 = set(map(int, input().split()))
y = int(input())
s2 = set(map(int, input().split()))
print(len(s1|s2))
