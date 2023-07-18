# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
res = re.search(r"([A-Za-z\d])\1+", input())
print(res.group(1)) if res else print(-1)
