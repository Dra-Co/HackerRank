# Enter your code here. Read input from STDIN. Print output to STDOUT
_, a = input(), input().split()
print(any([i == i[::-1] for i in a])and all([int(i) >= 0 for i in a]))
