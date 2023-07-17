# Enter your code here. Read input from STDIN. Print output to STDOUT
_, y = map(int, input().split())
print(*[sum(i)/y for i in list(zip(*[list(map(float, input().split())) for i in range(y)]))], sep="\n")
