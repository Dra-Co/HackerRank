# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input().split()
arr = input().split()
a = set(input().split())
b = set(input().split())
x = 0
for i in arr:
    if i in a:
        x += 1
    elif i in b:
        x -= 1
print(x)

