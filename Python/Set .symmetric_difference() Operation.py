# Enter your code here. Read input from STDIN. Print output to STDOUT
x = input()
a = set(input().split())
y = input()
b = set(input().split())
print(len(a^b))
