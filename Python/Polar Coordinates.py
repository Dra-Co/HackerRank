# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
n = complex(input())
print(abs(complex(n, 0.0)), phase(complex(n, 0.0)), sep="\n")
