# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
x = set(input().split())
b = input()
y = set(input().split())
print(*sorted(list(map(int, (x-y)|(y-x)))), sep="\n")
