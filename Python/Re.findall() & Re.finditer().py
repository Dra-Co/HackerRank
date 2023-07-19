# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
res = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])', input())
print(*res, sep="\n") if res else print(-1)
