# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = int(input()), int(input())
print(a//b, a%b, divmod(a,b), sep="\n")
