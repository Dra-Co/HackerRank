# Enter your code here. Read input from STDIN. Print output to STDOUT
_, a = int(input()), set(map(int, input().split()))
_, b = int(input()), set(map(int, input().split()))
print(len(a|b))
