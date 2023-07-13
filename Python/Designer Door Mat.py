# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
for i in range(1, n//2+1): 
    print((".|."*(i*2-1)).center(m, "-"))
print(("WELCOME").center(m,"-"))
for i in reversed(range(1, n//2+1)):
    print((".|."*(i*2-1)).center(m, "-"))
