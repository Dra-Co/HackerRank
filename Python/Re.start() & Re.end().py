# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s, p = input(),re.compile(input())
m = p.search(s)
if not m:
        print((-1,-1))  
while m:
    print((m.start(),m.end()-1))
    m = p.search(s,m.start()+1)
